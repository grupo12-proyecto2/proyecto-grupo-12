def buscador_reseñas (lista:list[dict]):
    '''
    Representamos una lista de alquileres y su cantidad de reseñas
    utilizando un diccionario que almacena el nombre del alquiler 
    como clave y sus reseñas como valor.

    buscador_reseñas: list[dict] -> Dict[str, int]

    El parametro es una lista de diccionarios donde cada diccionario
    representa los datos de un alquiler. El resultado es un diccionario
    con el nombre de los alquileres y su cantidad de reseñas.

    Ejemplos:
    1)
    Entrada: 
    [
    {"name": "Bright Modern Garden Unit - 1BR/1BTH", "number_of_reviews": 507, "last_review": "2025-11-15", "reviews_per_month": 2.54},
    {"name": "Creative Sanctuary", "number_of_reviews": 105, "last_review": "2017-08-06", "reviews_per_month": 0.52},
    {"name": "*FriendlyRoom Apt. Style -UCSF/USF - San Francisco", "number_of_reviews": 10, "last_review": "2023-07-30", "reviews_per_month": 0.07}
    ]
    Salida:
    {"Bright Modern Garden Unit - 1BR/1BTH":"507","Creative Sanctuary":"105","*FriendlyRoom Apt. Style -UCSF/USF","10"}
    2)
    Entrada:
    [
    {"name": "Bright Modern Garden Unit - 1BR/1BTH", , "last_review": "2025-11-15", "reviews_per_month": 2.54},
    {"name": "Creative Sanctuary", , "last_review": "2017-08-06", "reviews_per_month": 0.52},
    {"name": "*FriendlyRoom Apt. Style -UCSF/USF - San Francisco", , "last_review": "2023-07-30", "reviews_per_month": 0.07}
    ]
    Salida:
    {"Bright Modern Garden Unit - 1BR/1BTH":,"Creative Sanctuary":,"*FriendlyRoom Apt. Style -UCSF/USF - San Francisco":}
    3)
    Entrada:
    []
    Salida:
    {}
    '''
    diccionario_reseñas = {}
    for linea in lista:
        diccionario_reseñas[linea["name"]] = int(linea.get("number_of_reviews",0))
    return diccionario_reseñas
