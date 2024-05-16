import socket
import binascii
import re
import struct
import sys

def bytes_to_long(bytes_data):
    return int.from_bytes(bytes_data, 'big')

def save_response(response):
    try:
        with open("respuesta_hex.txt", "wb") as file:
            file.write(binascii.hexlify(response))
       #     print("Respuesta guardada en respuesta_hex.txt")
    except Exception as e:
        print("Error al guardar la respuesta:", e)

def send_with_saved_response(server_address, server_port, saved_response):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

     #   print("Enviando nueva solicitud con respuesta guardada:", saved_response)
        sock.sendto(saved_response, (server_address, server_port))
        response, _ = sock.recvfrom(1024)
        print("Respuesta del servidor usando respuesta guardada:")
        process_server_response(response)

        sock.close()
    except Exception as e:
        print("Error al enviar solicitud con respuesta guardada:", e)

def send_source_query(server_address, server_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        message_hex = "ffffffff553604445f"

        message = binascii.unhexlify(message_hex)

      #  print("Enviando mensaje:", message)
        sock.sendto(message, (server_address, server_port))

        response, _ = sock.recvfrom(1024)
       # print("Respuesta del servidor:", response)

        response = response.replace(b"\xffU", b"\xffA")
        response = response.replace(b"\xffA", b"\xffU")

        process_server_response(response)
        if len(response) < 10:
            save_response(response)
            send_with_saved_response(server_address, server_port, response)

        sock.close()
    except Exception as e:
        print("Error:", e)

def process_server_response(data):
    data = data.replace(b"\n", b"\xa6").replace(b"\x0A", b"\xa6")
    pattern = re.compile(b'\x00([\x20-\x7E\x80-\xFF]+)\x00(.)\x00\x00\x00(.*?)(.{3})(?=\x00[\x20-\x7E\x80-\xFF]+|\Z)')
    matches = pattern.findall(data)

 #   print("Información de jugadores:")

    for match in matches:
        name = match[0].decode('utf-8')
        
        score_byte = match[1]
        if score_byte == b"\xa6": 
            score = 10  
        else:
            score = bytes_to_long(score_byte)  

        time = match[2] + match[3] 
        
        float_value = struct.unpack('f', time)[0]
        
        hours = int(float_value // 3600)
        remaining_minutes = int((float_value % 3600) // 60)
        seconds = int(float_value % 60)
        
        time_played = ""
        if hours > 0:
            time_played += f"{hours} hora{'s' if hours > 1 else ''}, "
        if remaining_minutes > 0:
            time_played += f"{remaining_minutes} minuto{'s' if remaining_minutes > 1 else ''}, "
        if seconds > 0:
            time_played += f"{seconds} segundo{'s' if seconds > 1 else ''}"
        if time_played == "":
            time_played = "menos de 1 segundo"
        
        print(f"Nombre: {name}, Puntuación: {score}, Tiempo jugado: {time_played}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <dirección_IP_del_servidor> <puerto_del_servidor>")
        sys.exit(1)

    server_address = sys.argv[1]
    server_port = int(sys.argv[2])

    send_source_query(server_address, server_port)
