#Nombre: Eric Railef Mansilla
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


except requests.exceptions.Timeout:
    print("Error: se agoto el tiempo de espera")