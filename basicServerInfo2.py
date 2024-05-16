import socket
import re
import sys

def separar_texto(texto):
    palabras = re.findall(r'\\([^\\]+)', texto)
    return {i+1: palabra for i, palabra in enumerate(palabras)}

def send_source_query(server_address, server_port, output_file):
    try:
       
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        
        message = bytearray([
            0xFF, 0xFF, 0xFF, 0xFF, 
            ord('T'), ord('S'), ord('o'), ord('u'),
            ord('r'), ord('c'), ord('e'), ord(' '), 
            ord('E'), ord('n'), ord('g'), ord('i'), 
            ord('n'), ord('e'), ord(' '), ord('Q'), 
            ord('u'), ord('e'), ord('r'), ord('y'), 0x00 
        ])

        sock.sendto(message, (server_address, server_port))

        response, _ = sock.recvfrom(1024)

        with open(output_file, 'w') as file:
            textoServer = ("{}".format(response))
            texto = textoServer
            palabras = separar_texto(texto)
            for i, palabra in palabras.items():
                if i == 5:
                    palabra = palabra.replace("x00", "")
                    print("Nombre:", palabra)
                elif i == 6:
                    palabra = palabra.replace("x00", "")
                    print("Mapa:", palabra)
                elif i == 10:
                    palabra = palabra.replace("x", "")
                    palabra = palabra.replace("/dl", "")
                    print("Numero de jugadores:", palabra)

       
        sock.close()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <ip_del_servidor> <puerto_del_servidor>")
        sys.exit(1)

    server_address = sys.argv[1]
    server_port = int(sys.argv[2])
    output_file = "outpute.txt"  

    send_source_query(server_address, server_port, output_file)
