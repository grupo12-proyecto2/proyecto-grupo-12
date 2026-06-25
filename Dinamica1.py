import streamlit as st

def filtrar_barrios(lista:list[dict],opciones:str):
    '''
    Representamos una lista de alquileres (filtrada por el barrio que selecciono el usuario), mediante una lista.
    lista: Lista
    opciones: String

    filtrar_barrios: Lista String -> Lista
    El parámetro lista corresponde a la lista de alquileres general.
    El parámetro String corresponde al barrio seleccionado por el usuario.
    Devuelve la lista de alquileres cuyo barrio coincide
    con el seleccionado por el usuario.
    
    Ejemplo:
    lista = 
    [{"neighbourhood": "Nob hill"},
    {"neighbourhood": "Noe vallley"},
    {"neighbourhood": "Nob hill"}]

    opciones = "Nob hill"

    -->
    [  {"neighbourhood": "Nob hill"},
    {"neighbourhood": "Nob hill"}]
    '''   
    lista_filtrada=[]
    for linea in lista:
         if linea ["neighbourhood"]==opciones:
                lista_filtrada.append(linea) 
    return lista_filtrada 



def buscar_ubicacion(lista:list[dict]): 
   '''
   Recorre cada elemento de la lista,elimina el segundo punto de 
   los valores de latitud y longitud mediante la funcion sacar_punto
   los convierte a float y los almacena en las listas separadas
   Ejemplo:
   datos=[
   ...{"latitude": "12.345.678","longitude: "98.765.432"},
   "latitude": "11.222.333","longitude: "44.555.666"}...]-->
   {'lat':[12.345678,98.765432] 
   'lon':[11.222333,44.555666]}
   lista(list-diccionarios)--->dict
   '''    
   diccionario={}
   longitud=[]
   latitud=[]
   for linea in lista: 
        latitud.append(float(linea["latitude"]))
        longitud.append(float(linea["longitude"]))
   diccionario["lat"]=latitud 
   diccionario["lon"]=longitud
   
   return diccionario 