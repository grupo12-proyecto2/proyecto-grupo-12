#Pregunta 1: Cuales son los 5 barrios con mas alquileres 
import matplotlib.pyplot as plt

def buscador_barrio (alquiler,clase):
       '''
       Representamos los alquileres mediante una lista de diccionarios, cada lista
       tiene informacion de un hospedaje. 
       Alquiler representa una lista de hospedajes.

       alquiler: list  

       buscador_barrio: list -> dict

       la clave es el nombre del barrio y el valor la cantidad de hospedajes
       ejemplo: 
       buscador_barrio([])={} ejemplo que devuelve vacio .
       alquiler=[{"neighbourhud":"Bernal Heights"}]
       buscador_barrio(alquiler)={"Bernal Heights":1}
       alquiler1=[{"neighbourhud":"Crocker Amazon","price": 100,"room_type":"Entire home/apt"},
            {"neighbourhud":"Downtown/Civic Center","price":85,"room_type":"Private room"},
            {"neighbourhud":"Crocker Amazon","price":120,"room_type":"Entire home/apt"}]
        buscador_barrio(alquiler1)={"Crocker Amazon":2,"Downtown/Civic Center":1} 

       '''
       diccionario={}
       for linea in alquiler:
              diccionario[linea[clase]]=diccionario.get(linea[clase],0)+1
       return diccionario   


#version con dos ciclos
def barrios5 (barrios,cantidad):
    '''
    Representamos con un diccionario la cantidad de hospedajes por barrios
    barrios: dict
    barrios5: dict-> dict
    el parametro representa un diccionario. la clave es el nombre del barrio 
    y el valor la cantidad de hospedajes del barrio.
    La funcion retorna a un diccionario con los 5 barrios con mayor hospedajes.

    Ejemplo: 

    1)
    Entrada: {}
    Salida: {}

    2)
    Entrada: {"Mission":100,"Wester Addition":50,"Pacific Heights":40,
             "Dowtown/Civic Center":30,"Bernal Heights":20,"Haight Ashbury":10,
             "Noe Valley":5})

    Salida:  {"Mission":100,"Wester Addition":50,"Pacific Heights":40,
             "Dowtown/Civic Center":30,"Bernal Heights":20}

    3)
    Entrada: {"Mission":100,"Dowtown/Civic Center":30}

    Salida: {"Mission":100,"Dowtown/Civic Center":30}

    ''' 
    lista_5 = {}
    copia = barrios.copy()


    while len(lista_5) < cantidad and  list(copia.keys()) != []:
        maximo = 0

        for barrio in copia:
            if barrios[barrio] > maximo:
                maximo = barrios[barrio]
                barrio_max = barrio

        lista_5[barrio_max] = maximo
        
        
        if copia.get(barrio_max) != None:
            del copia[barrio_max]
    return lista_5

    
def grafico_barras (data,info_x,titulo):
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
 ax.set_xlabel(info_x)
 ax.set_title(titulo)
 return fig

