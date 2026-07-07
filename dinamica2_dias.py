#LIBRERIA
import streamlit as st

def filtrar_dias(lista:list[dict],dias:int)-> list[dict]:
     '''
     Filtra los alquileres
     Recibe una lista de alquileres y una cantidad de días,
     y devuelve únicamente los alquileres con
     disponibilidad de dias anuales (availability_365) sea mayor
     o igual al valor indicado.
     lista: son las listas de alquileres
     dias: son la cantidad de dias
     
     ejemplos:

     lista=
     ([{"availability_365": 276, "reviews_last_year": 2, "status": ""},
     {"availability_365": 301, "reviews_last_year": 0, "status": "pending"},
     {"availability_365": 211, "reviews_last_year": 1, "status": ""}]
     , 300)

     1) filtrar_dias(lista,300)

     ==> Devuelve
     [{"availability_365": 301, "reviews_last_year": 0, "status": "pending"}]

     2)
     filtrar_dias([], 200)

     ==> Devuelve 
     []  (lista vacia)

     3)
     filtrar_dias(lista,360)

     ==> Devuelve 
     []  (lista vacia)
     '''
     lista_filtrada=[]
     #Recorre todos los alquileres
     for linea in lista: 
         if int(linea ["availability_365"])>=dias:  #verifica si cumple con la cant. de dias
                #agrega el alquiler a la lista filtrada
                lista_filtrada.append(linea)  
     #Devuelve la lista filtrada
     return lista_filtrada   
     


    

