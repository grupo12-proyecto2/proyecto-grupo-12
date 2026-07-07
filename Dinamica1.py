#LIBRERIA
import streamlit as st
#=====================================================

def filtrar_barrios(lista:list[dict],opciones:str)->list:
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

    1)
    lista = 
    [{"neighbourhood": "Nob hill"},
    {"neighbourhood": "Noe vallley"},
    {"neighbourhood": "Nob hill"}]

    opciones = "Nob hill"

    --> Devuelve
    [  {"neighbourhood": "Nob hill"},
    {"neighbourhood": "Nob hill"}]

    2)
    lista = 
    [{"neighbourhood": "Nob hill"},
    {"neighbourhood": "Noe vallley"},
    {"neighbourhood": "Nob hill"}]

    opciones = "Potrero hill"

    --> Devuelve
    []

    3)
    lista = []

    opciones = "Potrero hill"

    --> Devuelve
    []

    '''   
    lista_filtrada=[]
    #Recorre cada alquiler de la lista
    for linea in lista:

         #verifica que coincida con el barrio indicado
         if linea ["neighbourhood"]==opciones:

               #agrega el alquiler a la lista filtrada
                lista_filtrada.append(linea) 
                
    return lista_filtrada 



def buscar_ubicacion(lista:list[dict])->dict: 
   '''
   Recorre cada elemento de la lista,elimina el segundo punto de 
   los valores de latitud y longitud mediante la funcion sacar_punto
   los convierte a float y los almacena en las listas separadas para
   devolverlos en un diccionario:
   Ejemplo:
   1)
   lista=[
   ...{"latitude": "12.345.678","longitude: "98.765.432"},
   "latitude": "11.222.333","longitude: "44.555.666"}...]
   --> Devuelve

   {'lat':[12.345678,98.765432] 
   'lon':[11.222333,44.555666]}

   2)
   lista= [{"neighbourhood": "Nob hill"},
   {"neighbourhood": "Noe vallley"},
   {"neighbourhood": "Nob hill"}]

   --> Devuelve
   {}   (diccionario vacio)
    
   3)
   lista=[]

   --> Devuelve
   {}  (diccionario vacio)
   '''    
   diccionario={}
   longitud=[]
   latitud=[]
   #recorre cada alquiler de la lista
   for linea in lista: 

     #obtiene la latitud y longitud y las convierte en tipo float
     latitud.append(float(linea["latitude"]))
     longitud.append(float(linea["longitude"]))

   #guarda las latitudes y longitudes en el diccionario.
   diccionario["lat"]=latitud 
   diccionario["lon"]=longitud

   #devuelve el diccionario con las listas
   return diccionario 