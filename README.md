# source-player-query-CS1.6
Herramienta que te permite obtener información detallada sobre los jugadores que están jugando en servidores de juegos basados en el motor de Source, como Counter-Strike: Global Offensive, Team Fortress 2, y otros.
# ES
### Características
Consulta rápida de los jugadores en un servidor de juegos de Source.
Muestra el nombre, la puntuación y el tiempo jugado de cada jugador.
Interfaz simple de línea de comandos para una fácil integración en scripts y aplicaciones.
Compatible con una variedad de juegos que utilizan el motor de Source.
# Uso
### Clonar el repositorio:
```sh
https://github.com/Linkmail16/source-player-query-CS1.6
```
### Ejecutar el script:
```sh
python source_player_info.py <dirección_IP_del_servidor> <puerto_del_servidor>
```
Reemplaza `<dirección_IP_del_servidor>` y `<puerto_del_servidor>` con la dirección IP y el puerto del servidor de juegos de Source que deseas consultar.
* Una vez que hayas ejecutado el script con los parámetros adecuados, verás la información detallada de los jugadores que están jugando en el servidor.
```sh
Nombre: JUNRBT, Puntuación: 4, Tiempo jugado: 20 minutos, 32 segundos
Nombre: Slazhed, Puntuación: 1, Tiempo jugado: 17 minutos, 4 segundos
Nombre: Player, Puntuación: 5, Tiempo jugado: 10 minutos, 7 segundos
```
Ejemplo
bash
Copy code
python source_player_info.py 192.168.1.100 27015
Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna idea para mejorar esta herramienta, por favor abre un issue o envía una pull request.

Licencia
Este proyecto está licenciado bajo la Licencia MIT.
