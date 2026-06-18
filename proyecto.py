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
'''
Representamos los alquileres mediante una lista de diccionarios, cada lista
tiene informacion de un hospedaje. 
Alquiler representa una lista de hospedajes.

alquiler: list  

buscador_barrio: list -> dict

la clave es el nombre del barrio y el valor la cantidad de hospedajes
ejemplo: 
buscador_barrio([{"neighbourhood": "Western Addition"}, {"neighbourhood": "Nob Hill"}])
=
{"Western Addition": 2, "Nob Hill": 1}
'''
       diccionario={}
       for linea in alquiler:
              diccionario[linea["neighbourhood"]]=diccionario.get(linea["neighbourhood"],0)+1
       return diccionario   

#version con recursion

def buscar_max(barrios,dicc_max={}):
''' 
Repreentamos con un diccionario la cantidad de hospedajes por barrio
buscar_max: dict,dict ->dict
barrios:dict
dicc_max:dict     
El parametro barrios representa un diccionario.
La clave es el nombre del barrio y el valor la cantidad de hospedajes.

El parametro dicc_max representa un diccionario que va almacenando los barrios con el maximo
numero de hospedajes.

La funcion retorna a un diccionario con los 5 barrios con mayor hospedajes.
'''
       max=0
       claves = list(barrios.keys())
       for x in claves:
              if barrios[x] > max:
                     max= barrios[x]
                     barrio_max= x
       dicc_max[barrio_max]=max
       if len(dicc_max)<5:
              copia=barrios.copy()
              del copia[barrio_max]
              return buscar_max (copia,dicc_max)
       else:
              return dicc_max

#version con dos ciclos
def barrios5 (barrios):
'''
Representamos con un diccionario la cantidad de hospedajes por barrios
barrios: dict
barrios5: dict-> dict
el parametro representa un diccionario. la clave es el nombre del barrio 
y el valor la cantidad de hospedajes del barrio.
La funcion retorna a un diccionario con los 5 barrios con mayor hospedajes.
ejemplo: 
''' 
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
 ax.yaxis.set_inverted(True)  
 ax.set_xlabel('Cantidad de alquileres')
 ax.set_title('Los 5 barrios con más alquileres')
 return fig

def menu (barrios):
   options=st.menu_button("Seleccione un barrio",barrios.keys())
   st.write("Seleccionaste:",options)
   return options 

def filtrar_barrios(lista,opciones):
    lista_filtrada=[]
    for linea in lista:
         if linea ["neighbourhood"]==opciones:
                lista_filtrada.append(linea) 
    return lista_filtrada 

def sacar_punto (num):
       punto1= num.find(".")
       punto2= num.find(".",punto1+1)
       num_nuevo=num[:punto2] + num[punto2+1:]
       return num_nuevo


def buscar_ubicacion(lista):
   diccionario={}
   longitud=[]
   latitud=[]
   for linea in lista: 
        print (linea)
        latitud.append(float(sacar_punto(linea["latitude"])))
        longitud.append(float(sacar_punto(linea["longitude"])))
   diccionario["lat"]=latitud 
   diccionario["lon"]=longitud
   
   return diccionario 
   

            

def main ():
         lista=Lectura_Archivo()
         barrios=buscador_barrio(lista)
         barrios_mayores= buscar_max(barrios) 
         #Pregunta Estática: Mostrar los 5 barrios con más alquileres
         st.pyplot(grafico_barras(barrios_mayores))
         opciones=menu(barrios)
         st.write(filtrar_barrios(lista,opciones))
         alquileres_filtrados=filtrar_barrios(lista,opciones)
         if opciones != None:
               ubicacion= buscar_ubicacion(alquileres_filtrados)
               st.map(ubicacion,size=20, color="#0044ff")
               st.write(ubicacion)
         
main()




