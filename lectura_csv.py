import csv

def lectura():
        '''
        Lee un archivo CSV y guarda cada linea como un diccionario adentro de una lista.

        Ejemplo:
        archivo:
        id,name,host_id,host_profile_id,host_name,neighbourhood_group,neighbourhood,
        958,"Bright, Modern Garden Unit - 1BR/1BTH",1169,1462506189282101689,Holly,
        ,Western Addition,
        - >
        [{"id": "958",
        "name": "Bright, Modern Garden Unit - 1BR/1BTH",
        "host_id": "1169",
        "host_profile_id": "1462506189282101689",
        "host_name": "Holly",
        "neighbourhood_group": "",
        "neighbourhood": "Western Addition"}]
        '''
        lista_alquileres = []
        #GUARDAR DATOS EN LISTAS
        with open ("listings-San Francisco.csv", newline='') as csvfile:
                 archivo =csv.DictReader(csvfile, delimiter=',', quotechar='"') 
                 for linea in archivo:
                         lista_alquileres.append(linea)
        return lista_alquileres


              
