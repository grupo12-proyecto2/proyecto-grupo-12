import streamlit as st

def filtrar_dias(lista:list[dict],dias:int):
     '''
     Representa una lista de alquileres filtrada por la cantidad de días
     con una lista de diccionarios.

     lista: lista de alquileres
     dias: cantidad de días

     filtrar_dias: List[dict] Int -> List[dict]

     filtrar_dias(
     [{"availability_365": 276, "reviews_last_year": 2, "status": ""},
     {"availability_365": 365, "reviews_last_year": 0, "status": "pending"},
     {"availability_365": 211, "reviews_last_year": 1, "status": ""}],300)
     ==
     [{"availability_365": 365, "reviews_last_year": 0, "status": "pending"}]
     '''
     lista_filtrada=[]
     for linea in lista:
         if int(linea ["availability_365"])>=dias:
                lista_filtrada.append(linea)
     return lista_filtrada 
     


    

