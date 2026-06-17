import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import codecs

def crear_diccionario (linea1):
 '''
 Representamos datos CSV, previamente almacenados en una lista, en un diccionario.
 Cada dato corresponde a cada categoría del archivo CSV.
 Clave: Categoría 
 Valor: Dato correspondiente
 PREGUNTA: Poner cada categoría, aunque algunas no se usen?
 linea1: Lista
 crear_diccionario: Lista -> Diccionario
 El parametro linea1 representa una lista, cuyos elementos serán almacenados
 en un diccionario.

 Ejemplos:
 crear_diccionario   
 PREGUNTA: Es necesario poner ejemplos de esto? Es posible probar esta funcion?
 '''
 x=0
 #Diccionario base
 diccionario_alquileres = {"id":" ","name":" ","host_id": " ","host_profile_id":" ","host_name": " ","neighbourhood_group": " ","neighbourhood":" ","latitude":" ","longitude":" ","room_type":" ","price":" ","minimum_nights":" ","number_of_reviews":" ","last_review":" ","reviews_per_month":" ","calculate_host_listing":" ","availability_365":" ","number_of_reviews":" ","license":" "} 
 claves = list(diccionario_alquileres.keys()) #Claves del diccionario en una lista
 while claves[x] != "license":
        diccionario_alquileres[claves[x]]=linea1[x]
        x=x+1
 else:
        diccionario_alquileres[claves[x]]=linea1[x] #Es necesario guardar la primer linea?
        x=0
 return diccionario_alquileres


#Lectura del csv 
def Lectura_Archivo (): 
 '''
 Representamos un archivo CSV, con una lista de diccionarios.
 Cada diccionario representa la información de un alquiler,
 es decir, de una línea del archivo CSV.
 Cada columna del archivo está representada en una clave del diccionario.

 lectura_Archivo: None -> Lista
        
 '''
 lista_alquileres = []
 i=0
 archivo1 = open ("Listing-prueba.csv")
 for linea in archivo1:
         linea=linea.strip("\n")
         linea=linea.split(",")
         if i>=1:
                 lista_alquileres.append(crear_diccionario(linea))
         if i==0:                 
                 i=i+1
 archivo1.close() #CIERRE 
 return lista_alquileres


def buscador_barrio (alquiler):
       diccionario={}
       for linea in alquiler:
              diccionario[linea["neighbourhood"]]=diccionario.get(linea["neighbourhood"],0)+1
       return diccionario       
#version con recursion
def buscar_max(barrios,dicc_max={}):
       max=0
       claves = list(barrios.keys())
       for x in claves:
              if barrios[x] > max:
                     max= barrios[x]
                     barrio_max= x
       dicc_max[barrio_max]=max
       if len(dicc_max)<5:
              del barrios[barrio_max]
              return buscar_max (barrios,dicc_max)
       else:
              return dicc_max

#version con dos ciclos
def barrios5 (barrios):
    lista_5 = {}

    while len(lista_5) < 5:
        maximo = 0
        barrio_max = ""

        for barrio in barrios:
            if barrios[barrio] > maximo:
                maximo = barrios[barrio]
                barrio_max = barrio

        lista_5[barrio_max] = maximo
        del barrios[barrio_max]

    return lista_5

    
def grafico_barras (data):
 fig, ax = plt.subplots()

 ax.barh(data.keys(), data.values(), align='center')
 ax.yaxis.set_inverted(True)  # arrange data from top to bottom
 ax.set_xlabel('Cantidad de alquileres')
 ax.set_title('Los 5 barrios con más alquileres')
 return fig

def menu (barrios):
   options=st.multiselect("Seleccione los barrios",barrios.keys(),accept_new_options=True)
   st.write("Seleccionaste:",options)
   return options 




def main ():
         lista=Lectura_Archivo()
         barrios=buscador_barrio(lista)
         barrios_mayores= buscar_max(barrios) 
         #Pregunta Estática: Mostrar los 5 barrios con más alquileres
         st.pyplot(grafico_barras(barrios_mayores))
         menu(barrios)

main()




