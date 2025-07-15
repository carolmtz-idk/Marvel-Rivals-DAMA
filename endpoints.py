from fastapi import APIRouter, Query, HTTPException  #APIRouter permite agrupar las rutas de archivos, Query es para validar y declarar parametros
from clases import Personaje, Origen, ElementosPOST #se importan las clases del archivo clases.py
from typing import List #ayuda a definir tipos de datos, osea una lista de personajes
import json #importamos para poder manejar archivos JSON
from pathlib import Path #Path es para manejar rutas de archivos
from datetime import datetime #maneja fechas actuales y horas.
import httpx

router = APIRouter()
RUTA_ARCHIVO = Path("personajes.json")

# TOKEN DE TWITTER/X
BEARER_TOKEN = "mi_token"  # <-- Reemplaza esto con tu token real
MARVEL_RIVALS_ID = "1649007859646072832"  # ID de la cuenta @MarvelRivals


#funcion para traer los personajes del archivo JSON
def cargar_personajes(): 
    if RUTA_ARCHIVO.exists():
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


#funcion para guardar los personajes en el archivo JSON
def guardar_personajes(lista):
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)


@router.get("/personajes", response_model=List[Personaje]) #le dice a FastAPI que la respuesta será una lista de objetos tipo Personaje.
def obtener_personajes( #esta es la funcion, no se puede cortar una funcion, asi que se manda a llamar la variable "personajes_data"
    pagina: int = Query(1, ge=1), #ge = es un metodo de validacion que significa "mayor o igual que"
    limite: int = Query(10, ge=1), #query = se usa para obtener los parametros de la url
):
    personajes = cargar_personajes()
    inicio = (pagina - 1) * limite
    fin = inicio + limite #Se mostrarán los elementos desde el índice 10 hasta el 19.
    return personajes[inicio:fin]


@router.post("/ElementosPOST/") #ruta para agregar un personaje
async def crear_item(item: ElementosPOST): #async es una funcion asincronica, se usa para manejar operaciones que puedan tardar, item es el objeto que se va a crear
    personajes = cargar_personajes() 
    
    nuevo = item.model_dump() #convierte el objeto a un diccionario

    if personajes:
        nuevoID = max(p["id"]for p in personajes) + 1 #obtenemos el ID maximo y le sumamos 1 para el nuevo objeto.
    else:
        nuevoID = 1

    nuevo["id"] = nuevoID
    nuevo["FechaCreacion"] = datetime.now().isoformat()
    
    ordenado = {
        "id": nuevo["id"],
        "Nombre": nuevo["Nombre"],
        "Universo": nuevo["Universo"],
        "RolDePersonaje": nuevo["RolDePersonaje"],
        "Armas": nuevo["Armas"],
        "Salud": nuevo["Salud"],
        "origen": nuevo["origen"],
        "FechaCreacion": nuevo["FechaCreacion"]
    }
    
    personajes.append(ordenado) #para agregar el nuevo personaje
    guardar_personajes(personajes) #se guarda el personaje en el JSON
    return {
        "mensaje": "Personaje agregado exitosamente",
        "personaje": ordenado
    }

@router.get("/personajes/media")
async def obtener_tweets_marvel():
    url = "https://api.twitter.com/2/tweets/search/recent"
    query = "from:MarvelRivals"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    params = {
        "query": query,
        "max_results": 10,
        "tweet.fields": "author_id,text,id"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        data = response.json()
        print(data)  # Aquí inspecciona la respuesta
    
        if response.status_code != 200:
            return {"error": "No se pudieron obtener los tweets", "detalle": data}
        
        tweets = data.get("data", [])
        # Procesa los tweets
        resultado = [{"id": t["id"], "texto": t["text"], "autor": t["author_id"]} for t in tweets]
        return resultado

@router.delete("/personajes/{personaje_id}", status_code=204)
def eliminar_personaje(personaje_id: int):
    personajes = cargar_personajes()
    personajes_filtrados = [p for p in personajes if p["id"] != personaje_id]
    
    if len(personajes) == len(personajes_filtrados):
        raise HTTPException(status_code=404, detail="Personaje no encontrado")

    guardar_personajes(personajes_filtrados)
    return


