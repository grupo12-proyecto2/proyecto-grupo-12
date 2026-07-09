import csv

def lectura(archivo_csv):
        '''
        Lee un archivo CSV y guarda cada linea como un diccionario adentro de una lista.
        Los valores de la primer línea se utilizan como las claves del diccionario.

        Ejemplo:

        1)
        Entrada:
        (Listing-prueba.csv)
        id,name,host_id,host_profile_id,host_name,neighbourhood_group,neighbourhood,latitude,longitude,room_type,price,minimum_nights,number_of_reviews,last_review,
        reviews_per_month,calculated_host_listings_count,availability_365,number_of_reviews_ltm,license
        958,    Bright Modern Garden Unit - 1BR/1BTH,1169,1462506189282101689,Holly,,Western Addition,37.77028,-122.43317,Entire home/apt,,2,507,2025-11-15,2.54,1,
        228,41,STR-0006854
        5858,Creative Sanctuary,8904,1462506623299518225,Philip Jonathon,,Bernal Heights,37.74474,-122.42089,Entire home/apt,,30,105,2017-08-06,0.52,1,365,0,
        8142,*FriendlyRoom Apt. Style -UCSF/USF - San Francisco,21994,1462506956810615042,Aaron,,Haight Ashbury,37.76555,-122.45213,Private room,,32,10,2023-07-30,
        0.07,20,362,0,
        8339,Historic Alamo Square Victorian,24215,1462506994551169471,Rosmarie,,Western Addition,37.77377,-122.43614,Entire home/apt,,9,25,2019-06-28,0.13,1,339,0,
        STR-0000264
        10537,Elegant & Cozy w/City views. Private room: Purple,36752,1462507288958203289,Teresa,,Bayview,37.7175,-122.39698,Private room,,1,46,2025-11-07,0.24,3
        ,365,12,2022-011003STR
        - >
        Salida:
        [{"id": "958",
        "name": "Bright, Modern Garden Unit - 1BR/1BTH",
        "host_id": "1169",
        "host_profile_id": "1462506189282101689",
        "host_name": "Holly",
        "neighbourhood_group": "",
        "neighbourhood": "Western Addition"}]

        2)
        Entrada:
        


        '''

        lista_alquileres = []
        #GUARDAR DATOS EN LISTAS
        with open (archivo_csv, newline='') as csvfile:
                 archivo =csv.DictReader(csvfile, delimiter=',', quotechar='"') 
                 for linea in archivo:
                         lista_alquileres.append(linea)
        return lista_alquileres


              
