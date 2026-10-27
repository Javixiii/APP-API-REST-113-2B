#Nombre: Javier Castro Galvez   
#Aplicacion API-REST

import requests

#api de productos de DummyJSON

BASE_URL= "https://dummyjson.com/products"

def mostrar_respuesta(respuesta):
    #mostrar el codigo HTTP y los datos resividos
    print("Codigo HTTP", respuesta.status_code)

    if respuesta.text:
        print("Respuesta JSON: ")
        print(respuesta.json())
    else:
        print("La respuesta no tiene datos")


try:
    # =============================
    # 1. GET: consultar un producto
    # =============================
    print("\n ---- GET - Consultar un producto ----")
    respuesta = requests.get(
        f"{BASE_URL}/19",
        timeout=10
    )

    respuesta.raise_for_status()
    producto = respuesta.json()

    print("Producto", producto["title"])
    print("Precio", producto["price"])
    print("Categoria", producto["category"])

    # ==========================
    # 2. metodo post
    # ==========================
    print("\n ---- POST - Crear un producto ----")

    nuevo_producto = {
        "title": "Teclado mecanico Gamer",
        "price": 90000,
        "description": "teclado para juegos",
        "categoty": "electronics"
    }

    respuesta = requests.post(
        f"{BASE_URL}/add",
        json=nuevo_producto,
        timeout=10
    )

    respuesta.raise_for_status()
    mostrar_respuesta(respuesta)

    print("Error: se agoto el tiempo de espera")

    # ==========================
    # 3. metodo PUT
    # ==========================

    print("\n ---- PUT - Actualizar un producto ----")

    producto_actualizado = {
        "title": "Notebook para desarrollar",
        "price": 590000,
        "description": "Notebook para programar",
        "categoty": "Laptops"
    }

    respuesta = requests.put(
        f"{BASE_URL}/1",
        json=producto_actualizado,
        timeout=10
    )

    respuesta.raise_for_status()
    mostrar_respuesta(respuesta)

except requests.exceptions.Timeout:
    print("Error: se agoto el tiempo de espera")