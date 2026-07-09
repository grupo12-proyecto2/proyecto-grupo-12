#LIBRERIA
import streamlit as st


def filtrar_por_habitacion(alquileres:list,habitaciones:list)->list:
    """
    Recibe una lista de alquileres y una lista tipo de habitacion y devuelve
    una lista con los alquileres que tengan los tipos de habitacion dados.
    ejemplos:

    lista = [{...,"room_type": "Private room","neighbourhood": "Nob hill"...},
    {---"room_type": "Shared room","neighbourhood": "Nob hill"...},
    {..."room_type": "Entire home/apt", "neighbourhood": "Nob hill"...}]

    1)
    filtrar_por_habitacion(lista,["Private room","Shared room"])

    --> Devuelve

    [{..."room_type": "Private room", "neighbourhood": "Nob hill"...},
    {..."room_type": "Shared room", "neighbourhood": "Nob hill"...}]

    2)
    filtrar_por_habitacion(lista,["room"])

    --> Devuelve

    []  (lista vacia)

    3)
    filtrar_por_habitacion([],"Shared room")

    --> Devuelve

    []   (lista vacia)

    """

    lista_filtrada=[]
    for linea in alquileres:
        if linea ["room_type"] in habitaciones:
            lista_filtrada.append(linea)
    return lista_filtrada

def tipo_habitaciones (alquileres:list)->list:
    """
    recibe una lista de alquileres y devuelve los distintos tipos de 
    habitaciones que existen en ella.
    ejemplos:
    1)
    tipo_habitaciones([])
    --> Devuelve 
    [] lista vacia 

    2)
    tipo_habitaciones([{..."room_type": "Private room", "neighbourhood": "Nob hill"...},
    {..."room_type": "Shared room", "neighbourhood": "Nob hill"...}])

    --> Devuelve

    ["Private room","Shared room"]

    3)
    tipo_habitaciones([{ "neighbourhood": "Nob hill"}])

    --> devuelve
    []    (lista vacia)
    """
    tipos=[]
    for linea in alquileres:
        if "room_type" in linea:
            if linea ["room_type"] not in tipos:
                tipos.append(linea["room_type"])
    return tipos