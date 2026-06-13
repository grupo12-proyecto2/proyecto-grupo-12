import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import codecs

#Decidimos usar diccionarios para almacenar la información de cada casa.
#Cada uno de los diccionarios estará almacenada en una lista.

lista_alquileres = []

#Lectura del csv 
archivo1 = open ("Listing-prueba.csv")
for linea in archivo1:
       linea=linea.strip("\n")
       lista_alquileres.append(tuple(linea.split(",")))
       


archivo1.close() #CIERRE 

print(lista_alquileres[0])
print(lista_alquileres[1])















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