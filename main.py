from pydantic import BaseModel #Se usa para crear clases que validan y definen el formato de los datos
from fastapi import FastAPI, Query # librería moderna para crear APIs.
from typing import List #se usa para decir que un valor será una lista de algo

class Origen(BaseModel): #esto es el origen del personaje
    nombre: str
    url: str

class Personaje(BaseModel): #caracteristicas de un personaje
    id: int #int = tipo de dato numerico entero
    Nombre: str #str = tipo de dato de texto
    Universo: str
    Rol_en_el_Juego: str
    Armas: str
    Salud: int
    origen: Origen

app = FastAPI() #instancia de la aplicacion 

personajes_data = [ #esta solo es la lista de los datos, se define la lista fuera de la funcion que es "obtener_personajes"
        {
            "id": 1,
            "Nombre": "Capitán América",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Vanguardia",
            "Armas": "Escudo",
            "Salud": 100,
            "origen": {
                "nombre": "Tierra",
                "url": "https://marvel.com/earth"
            }
        },
        {
            "id": 2,
            "Nombre": "Iron Man",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Vanguardia",
            "Armas": "Repulsores",
            "Salud": 100,
            "origen": {
                "nombre": "Tierra",
                "url": "https://marvel.com/ironman"
            }
        },
        {
            "id": 3,
            "Nombre": "Spider-Man",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Movilidad",
            "Armas": "Telarañas",
            "Salud": 90,
            "origen": {
                "nombre": "Tierra",
                "url": "https://marvel.com/spiderman"
            }
        },
        {
            "id": 4,
            "Nombre": "Loki",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Control",
            "Armas": "Magia",
            "Salud": 80,
            "origen": {
                "nombre": "Asgard",
                "url": "https://marvel.com/loki"
            }
        },
        {
            "id": 5,
            "Nombre": "Doctor Strange",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Soporte",
            "Armas": "Hechizos",
            "Salud": 90,
            "origen": {
                "nombre": "Tierra",
                "url": "https://marvel.com/doctorstrange"
            }
        },
        {
            "id": 6,
            "Nombre": "Magneto",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Control",
            "Armas": "Magnetismo",
            "Salud": 100,
            "origen": {
                "nombre": "Tierra",
                "url": "https://marvel.com/magneto"
            }
        },
        {
            "id": 7,
            "Nombre": "Storm",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Movilidad",
            "Armas": "Clima",
            "Salud": 90,
            "origen": {
                "nombre": "África",
                "url": "https://marvel.com/storm"
            }
        },
        {
            "id": 8,
            "Nombre": "Scarlet Witch",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Control",
            "Armas": "Magia del Caos",
            "Salud": 85,
            "origen": {
                "nombre": "Sokovia",
                "url": "https://marvel.com/scarletwitch"
            }
        },
        {
            "id": 9,
            "Nombre": "Rocket Raccoon",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Daño",
            "Armas": "Armas pesadas",
            "Salud": 80,
            "origen": {
                "nombre": "Halfworld",
                "url": "https://marvel.com/rocket"
            }
        },
        {
            "id": 10,
            "Nombre": "Groot",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Soporte",
            "Armas": "Ramas",
            "Salud": 120,
            "origen": {
                "nombre": "Planeta X",
                "url": "https://marvel.com/groot"
            }
        },
        {
            "id": 11,
            "Nombre": "Ironheart",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Vanguardia",
            "Armas": "Armadura",
            "Salud": 95,
            "origen": {
                "nombre": "Tierra",
                "url": "https://marvel.com/ironheart"
            }
        },
        {
            "id": 12,
            "Nombre": "Luna Snow",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Soporte",
            "Armas": "Hielo",
            "Salud": 85,
            "origen": {
                "nombre": "Corea del Sur",
                "url": "https://marvel.com/lunasnow"
            }
        },
        {
            "id": 13,
            "Nombre": "Peni Parker",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Movilidad",
            "Armas": "Robot SP//dr",
            "Salud": 90,
            "origen": {
                "nombre": "Tierra-14512",
                "url": "https://marvel.com/peniparker"
            }
        },
        {
            "id": 14,
            "Nombre": "Black Panther",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Vanguardia",
            "Armas": "Garras",
            "Salud": 95,
            "origen": {
                "nombre": "Wakanda",
                "url": "https://marvel.com/blackpanther"
            }
        },
        {
            "id": 15,
            "Nombre": "Namor",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Control",
            "Armas": "Tridente",
            "Salud": 100,
            "origen": {
                "nombre": "Atlántida",
                "url": "https://marvel.com/namor"
            }
        },
        {
            "id": 16,
            "Nombre": "Hela",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Control",
            "Armas": "Espadas mágicas",
            "Salud": 95,
            "origen": {
                "nombre": "Hel",
                "url": "https://marvel.com/hela"
            }
        },
        {
            "id": 17,
            "Nombre": "Venom",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Vanguardia",
            "Armas": "Simbionte",
            "Salud": 110,
            "origen": {
                "nombre": "Tierra",
                "url": "https://marvel.com/venom"
            }
        },
        {
            "id": 18,
            "Nombre": "The Punisher",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Daño",
            "Armas": "Arsenal",
            "Salud": 90,
            "origen": {
                "nombre": "Tierra",
                "url": "https://marvel.com/punisher"
            }
        },
        {
            "id": 19,
            "Nombre": "Wolverine",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Vanguardia",
            "Armas": "Garras",
            "Salud": 120,
            "origen": {
                "nombre": "Canadá",
                "url": "https://marvel.com/wolverine"
            }
        },
        {
            "id": 20,
            "Nombre": "Deadpool",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Daño",
            "Armas": "Katana",
            "Salud": 95,
            "origen": {
                "nombre": "Tierra",
                "url": "https://marvel.com/deadpool"
            }
        },
        {
            "id": 21,
            "Nombre": "Ghost-Spider",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Movilidad",
            "Armas": "Telarañas",
            "Salud": 90,
            "origen": {
                "nombre": "Tierra-65",
                "url": "https://marvel.com/ghostspider"
            }
        },
        {
            "id": 22,
            "Nombre": "Ms. Marvel",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Soporte",
            "Armas": "Elasticidad",
            "Salud": 85,
            "origen": {
                "nombre": "Jersey City",
                "url": "https://marvel.com/msmarvel"
            }
        },
        {
            "id": 23,
            "Nombre": "She-Hulk",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Vanguardia",
            "Armas": "Fuerza",
            "Salud": 110,
            "origen": {
                "nombre": "Tierra",
                "url": "https://marvel.com/shehulk"
            }
        },
        {
            "id": 24,
            "Nombre": "Blade",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Daño",
            "Armas": "Espada",
            "Salud": 100,
            "origen": {
                "nombre": "Tierra",
                "url": "https://marvel.com/blade"
            }
        },
        {
            "id": 25,
            "Nombre": "Spawn",
            "Universo": "Marvel",
            "Rol_en_el_Juego": "Daño",
            "Armas": "Magia",
            "Salud": 100,
            "origen": {
                "nombre": "Tierra",
                "url": "https://marvel.com/spawn"
            }
        }
    ]

#funcion para la paginacion, se pone al final porque una funcion no puede usar una variable que no esta definida primero, en este caso "personajes_data"
@app.get("/personajes", response_model=list[Personaje]) #le dice a FastAPI que la respuesta será una lista de objetos tipo Personaje.
def obtener_personajes( #esta es la funcion, no se puede cortar una funcion, asi que se manda a llamar la variable "personajes_data"
    pagina: int = Query(1, ge=1), #ge = es un metodo de validacion que significa "mayor o igual que"
    limite: int = Query(10, ge=1), #query = se usa para obtener los parametros de la url
):
    inicio = (pagina - 1) * limite
    fin = inicio + limite #Se mostrarán los elementos desde el índice 10 hasta el 19.
    return personajes_data[inicio:fin]




