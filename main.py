from fastapi import FastAPI, Request, HTTPException, Query, Header# librería para crear APIs.
from endpoints import router
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI() #instancia de la aplicacion 
app.include_router(router) #este conecta los endpoints a la aplicacion FastAPI

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errores = []
    for err in exc.errors():
        campo = err.get("loc")[-1]  # el nombre del campo que falla
        mensaje = err.get("msg")    # el mensaje de error original
        errores.append(f"El campo '{campo}' es requerido. {mensaje}")

    return JSONResponse(
        status_code=422,
        content={"mensaje_error": errores},
    )


TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

@app.get("/personajes/media")
def personajes_media(
    tema: str = Query("Marvel Rivals", description="Tema para buscar tweets")
):
    if not TWITTER_BEARER_TOKEN:
        raise HTTPException(status_code=500, detail="Token de Twitter no configurado")

    url = "https://api.twitter.com/2/tweets/search/recent"
    headers = {
        "Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"
    }
    params = {
        "query": tema,
        "max_results": 5,
        "tweet.fields": "created_at,author_id"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Aquí puede lanzar HTTPError

        # Mostrar cuántas peticiones quedan
        remaining = response.headers.get("x-rate-limit-remaining", "desconocido")
        print(f"Peticiones restantes: {remaining}")

        data = response.json()

        tweets = [
            {
                "id": t["id"],
                "text": t["text"],
                "author_id": t["author_id"],
                "created_at": t["created_at"]
            }
            for t in data.get("data", [])
        ]

        return JSONResponse(content=tweets)

    except requests.HTTPError as e:
        if e.response.status_code == 429:
            reset_time = e.response.headers.get("x-rate-limit-reset")
            raise HTTPException(
                status_code=429,
                detail=f"Límite de peticiones alcanzado. Intenta más tarde. Reinicio en UNIX: {reset_time}"
            )
        else:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"No se pudieron obtener los tweets: {str(e)}")




