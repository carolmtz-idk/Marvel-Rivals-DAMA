from fastapi import APIRouter, Query, HTTPException  #APIRouter permite agrupar las rutas de archivos, Query es para validar y declarar parametros
from clases import Personaje, Origen, ElementosPOST #se importan las clases del archivo clases.py
from typing import List, Optional #ayuda a definir tipos de datos, osea una lista de personajes
import json #importamos para poder manejar archivos JSON
from pathlib import Path #Path es para manejar rutas de archivos
from datetime import datetime #maneja fechas actuales y horas.
import httpx
from fastapi.responses import JSONResponse
from starlette.status import HTTP_429_TOO_MANY_REQUESTS

router = APIRouter()
RUTA_ARCHIVO = Path("personajes.json")

# TOKEN DE TWITTER/X
BEARER_TOKEN = "mi-token"  # <-- Reemplaza esto con tu token real
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
    pagina: Optional[int] = Query(None, ge=1), #ge = es un metodo de validacion que significa "mayor o igual que"
    limite: int = Query(10, ge=1), #query = se usa para obtener los parametros de la url
):
    personajes = cargar_personajes()
    if pagina is not None:
        inicio = (pagina - 1) * limite
        fin = inicio + limite
        return personajes[inicio:fin]
    else:
        # Si no se especifica página, devolvemos todo
        return personajes

@router.post("/personajes/ElementosPOST")
async def crear_item(item: ElementosPOST):
    personajes = cargar_personajes()
    nuevo = item.model_dump()

    # Validar si ya existe un personaje con el mismo nombre
    for p in personajes:
        if p["Nombre"].strip().lower() == nuevo["Nombre"].strip().lower():
            raise HTTPException(
                status_code=409,
                detail=f"Ya existe un personaje con el nombre '{nuevo['Nombre']}'"
            )
    if personajes:
        nuevoID = max(p["id"] for p in personajes) + 1
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

    personajes.append(ordenado)
    guardar_personajes(personajes)

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
            return JSONResponse(
                status_code=response.status_code,
                content={
                    "error": "No se pudieron obtener los tweets, demasiados intentos",
                    "detalle": data
                }
            )
        
        tweets = data.get("data", [])
        # Procesa los tweets
        resultado = [{"id": t["id"], "texto": t["text"], "autor": t["author_id"]} for t in tweets]
        return resultado

@router.delete("/personajes/{personaje_id}", status_code=200)
def eliminar_personaje(personaje_id: int):
    personajes = cargar_personajes()
    personajes_filtrados = [p for p in personajes if p["id"] != personaje_id]
    
    if len(personajes) == len(personajes_filtrados):
        raise HTTPException(status_code=404, detail="Personaje no encontrado")

    guardar_personajes(personajes_filtrados)
    return {"mensaje": "Personaje eliminado correctamente"}


@router.get("/personajes/{personaje_id}", response_model=dict)
def obtener_personaje(personaje_id: int):
    personajes = cargar_personajes()
    for personaje in personajes:
        if personaje["id"] == personaje_id:
            return personaje
    raise HTTPException(status_code=404, detail=f"No se encontró el personaje con ID {personaje_id}")




