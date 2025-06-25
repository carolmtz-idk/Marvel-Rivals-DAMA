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






