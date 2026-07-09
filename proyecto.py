#LIBRERIAS
import numpy as np
import streamlit as st
#FUNCIONES DE MODULOS
from lectura_csv import lectura
from Estatica1 import buscador_barrio,barrios5,grafico_barras
from Dinamica1 import filtrar_barrios,buscar_ubicacion
from dinamica2_dias import filtrar_dias

# ==================================================
# MAIN
# ==================================================
def main ():
         # ---------- LECTURA CSV ----------: 
         lista=lectura("Listing-prueba.csv")
          

         #---------- Formato de página ----------
         col1, col2 = st.columns(2,gap="large")

         #----------PREGUNTA ESTÁTICA: 5 barrios con más alquileres----------
         barrios=buscador_barrio(lista)
         barrios_mayores= barrios5(barrios) 
         grafico= grafico_barras(barrios_mayores)
         
         #----------PREGUNTA DINÁMICA: Mapeo de alquileres----------
         col1.subheader("Mapa de alquileres por barrio")
         opcion=col1.selectbox("Seleccione un barrio",barrios) #Despliegue de menú y guarda
         alquileres_filtrados=filtrar_barrios(lista,opcion)
         ubicacion= buscar_ubicacion(alquileres_filtrados)
         col1.map(ubicacion,size=20, color="#0044ff")

         #----------PREGUNTA DINÁMICA: Tabla de alquileres con X disponibilidad de días---------- 
         rango_dias= list(range(1,366))
         col2.subheader("Disponibilidad de alquileres según días disponibles")    
         dias = col2.select_slider("Cantidad de días",rango_dias) 
         lista_dias=filtrar_dias(lista,dias)
         col2.write(f"Alquileres disponibles con {dias} días disponibles")
         col2.dataframe(lista_dias)
         
         #----------Muestra de Gráfico----------
         col1.subheader("ESTADISTICA: Los 5 barrios con mas alquileres")
         col1.pyplot (grafico)
# ==================================================
# MAIN
# ==================================================         

#LLAMADO DE MAIN
main()






