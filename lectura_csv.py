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
        - >
        Salida:
        [
        {
        "id": "958",
        "name": "Bright Modern Garden Unit - 1BR/1BTH",
        "host_id": "1169",
        "host_profile_id": "1462506189282101689",
        "host_name": "Holly",
        "neighbourhood_group": "",
        "neighbourhood": "Western Addition",
        "latitude": "37.77028",
        "longitude": "-122.43317",
        "room_type": "Entire home/apt",
        "price": "",
        "minimum_nights": "2",
        "number_of_reviews": "507",
        "last_review": "2025-11-15",
        "reviews_per_month": "2.54",
        "calculated_host_listings_count": "1",
        "availability_365": "228",
        "number_of_reviews_ltm": "41",
        "license": "STR-0006854"
        },
        {
        "id": "5858",
        "name": "Creative Sanctuary",
        "host_id": "8904",
        "host_profile_id": "1462506623299518225",
        "host_name": "Philip Jonathon",
        "neighbourhood_group": "",
        "neighbourhood": "Bernal Heights",
        "latitude": "37.74474",
        "longitude": "-122.42089",
        "room_type": "Entire home/apt",
        "price": "",
        "minimum_nights": "30",
        "number_of_reviews": "105",
        "last_review": "2017-08-06",
        "reviews_per_month": "0.52",
        "calculated_host_listings_count": "1",
        "availability_365": "365",
        "number_of_reviews_ltm": "0",
        "license": ""
        },
        {
        "id": "8142",
        "name": "*FriendlyRoom Apt. Style -UCSF/USF - San Francisco",
        "host_id": "21994",
        "host_profile_id": "1462506956810615042",
        "host_name": "Aaron",
        "neighbourhood_group": "",
        "neighbourhood": "Haight Ashbury",
        "latitude": "37.76555",
        "longitude": "-122.45213",
        "room_type": "Private room",
        "price": "",
        "minimum_nights": "32",
        "number_of_reviews": "10",
        "last_review": "2023-07-30",
        "reviews_per_month": "0.07",
        "calculated_host_listings_count": "20",
        "availability_365": "362",
        "number_of_reviews_ltm": "0",
        "license": ""
        }
        ]
        '''
        lista_alquileres = []
        #GUARDAR DATOS EN LISTAS
        with open (archivo_csv, newline='') as csvfile:
                 archivo =csv.DictReader(csvfile, delimiter=',', quotechar='"') 
                 for linea in archivo:
                         lista_alquileres.append(linea)
        return lista_alquileres


              
