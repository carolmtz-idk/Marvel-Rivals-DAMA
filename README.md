# API de Personajes de Marvel Rivals

Una API desarrollada en Python que permite gestionar personajes del universo **Marvel Rivals**. El proyecto permite **agregar personajes nuevos**, realizar **paginación de resultados**, y está conectado con **X (Twitter)** para obtener publicaciones recientes relacionadas con *Marvel Rivals*.

## Tecnologías usadas
- Python
- FastAPI
- Uvicorn
- JSON
- X/Twitter API
- Thunder Client o Postman (para pruebas)


## Instalación y ejecución
-Instalacion de las dependencias:
pip install fastapi uvicorn

-Ejecuta el servidor:
python -m uvicorn main:app --reload

-Haz la prueba en Thunder Client con la URL
-http://127.0.0.1:8000


## Almacenamiento
Los datos de los personajes se almacenan en un archivo .json, sin uso de base de datos externa.


## Funcionalidades
Ver listado de personajes (con paginación).

Agregar nuevos personajes vía endpoints.

Obtener publicaciones recientes desde X (Twitter) relacionadas con Marvel Rivals.


| Método | Endpoint      | Descripción                                  |
| ------ | ------------- | -------------------------------------------- |
| GET    | `/personajes` | Obtener lista de personajes (con paginación) |
| POST   | `/ElementosPOST/` | Agregar un nuevo personaje               |
| GET    | `/personajes/media` | Obtener tweets recientes sobre Marvel Rivals |


## En desarrollo activo
Esta API está en construcción, pero ya tiene funciones principales como lectura y escritura de personajes, paginación y conexión con X (Twitter). Se planean futuras mejoras como edición y eliminación de personajes.


## Autores
María Fernanda Morán Rodea
https://github.com/fernanda-91

Álvaro Fabián Ovalle Antonio
https://github.com/Fabian-o11

Allan Daniel Soria Palomo
https://github.com/ALLAN101101

Diana Carolina García Martínez

Kevin Joshua Lopez Iracheta
https://github.com/joshua085


