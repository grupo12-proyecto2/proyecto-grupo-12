import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import codecs

#Decidimos usar diccionarios para almacenar la información de cada casa.
#Cada uno de los diccionarios estará almacenada en una lista.


def crear_diccionario (linea1):
        x=0
        #Diccionario base
        diccionario_alquileres = {"id":" ","name":" ","host_id": " ","host_profile_id":" ","host_name": " ","neighbourhood_group": " ","neighbourhood":" ","latitude":" ","longitude":" ","room_type":" ","price":" ","minimum_nights":" ","number_of_reviews":" ","last_review":" ","reviews_per_month":" ","calculate_host_listing":" ","availability_365":" ","number_of_reviews":" ","license":" "} 
        claves = list(diccionario_alquileres.keys()) #Claves del diccionario en una lista
        while claves[x] != "license":
         diccionario_alquileres[claves[x]]=linea1[x]
         x=x+1
        else:
         diccionario_alquileres[claves[x]]=linea1[x]
         x=0
        return diccionario_alquileres


#Lectura del csv 
def Lectura_Archivo (): 
 lista_alquileres = []
 i=0
 archivo1 = open ("Listing-prueba.csv")
 for linea in archivo1:
         linea=linea.strip("\n")
         linea=linea.split(",")
         if i>=1:
                 lista_alquileres.append(crear_diccionario(linea))
         if i==0:
                 lista_alquileres.append(linea)
                 i=i+1
 archivo1.close() #CIERRE 
 return lista_alquileres
      
       
def main ():
         lista=Lectura_Archivo()
         print(lista)

main()

















#Pregunta Estática: Mostrar los 5 barrios con más alquileres

#Grafico de barras
plt.style.use('_mpl-gallery')

# make data:
x = 0.5 + np.arange(8)
y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()

st.pyplot(fig)