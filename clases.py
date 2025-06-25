from pydantic import BaseModel #Se usa para crear clases que validan y definen el formato de los datos

class Origen(BaseModel): #esto es el origen del personaje
    nombre: str
    url: str

class Personaje(BaseModel): #caracteristicas de un personaje
    id: int #int = tipo de dato numerico entero
    Nombre: str #str = tipo de dato de texto
    Universo: str
    RolDePersonaje: str
    Armas: str
    Salud: int
    origen: Origen

class ElementosPOST(BaseModel):
    Nombre: str
    Universo: str
    RolDePersonaje: str
    Armas: str
    Salud: int
    origen: Origen

