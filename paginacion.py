import requests

url = "http://127.0.0.1:8000/personajes"

for pagina in range(1, 4):  # Páginas 1, 2 y 3
    params = {"pagina": pagina, "limite": 10}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        personajes = response.json()
        print(f"Página {pagina} ({len(personajes)} personajes):")
        for p in personajes:
            print(f"- {p['Nombre']}")
        print()
    else:
        print(f"Error en página {pagina}: {response.status_code}")


#poder agregar un elemento a la lista desde el TC

 
