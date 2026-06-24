#Pregunta 1: Cuales son los 5 barrios con mas alquileres 
import matplotlib.pyplot as plt

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
    copia = barrios.copy()

    while len(lista_5) < 5:
        maximo = 0

        for barrio in copia:
            if barrios[barrio] > maximo:
                maximo = barrios[barrio]
                barrio_max = barrio

        lista_5[barrio_max] = maximo
        
        del copia[barrio_max]

    return lista_5

    
def grafico_barras (data):
 '''
 Representamos un diccionario con los 5 barrios con más alquileres, y las cantidades de alquileres
 mediante un gráfico de barras.
 data: Diccionario

 grafico_barras: Diccionario -> Gráfico de barras
 El parámetro es un diccionario con barrios, y la cantidad de alquileres en cada uno.
 Devuelve un gráfico de barras, donde en X se muestran los barrios y en Y n de alquileres.

 '''      
 fig, ax = plt.subplots()

 ax.barh(data.keys(), data.values(), align='center')
 ax.yaxis.set_inverted(True)  
 ax.set_xlabel('Cantidad de alquileres')
 ax.set_title('Los 5 barrios con más alquileres')
 return fig

