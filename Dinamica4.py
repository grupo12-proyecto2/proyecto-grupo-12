#PREGUNTA DINAMICA: Fue reseñada en el último año?
def filtro_ultimo_año (alquileres:list[dict],fue_reseñada:bool):
    '''
    Representamos una lista de alquileres usando una lista de diccionarios.
    
    filtro_ultimo_año: list[dict] bool -> list[dict]
    alquileres representa la lista de alquileres a filtrar
    fue_reseñada representa el estado de un Selectbox
    Si es "True" se ejecuta el filtro
    (Se eliminan los alquileres sin reseñas en 2025)
    Si es "False" se mantiene la lista

    Ejemplos:
    1)
    Entrada:
    [
    {"name": "Bright Modern Garden Unit - 1BR/1BTH", "number_of_reviews": 507, "last_review": "2025-11-15", "reviews_per_month": 2.54},
    {"name": "Creative Sanctuary", "number_of_reviews": 105, "last_review": "2017-08-06", "reviews_per_month": 0.52},
    {"name": "*FriendlyRoom Apt. Style -UCSF/USF - San Francisco", "number_of_reviews": 10, "last_review": "2023-07-30", "reviews_per_month": 0.07}
    ]
    ,True
    Salida:
    [
    {"name": "Bright Modern Garden Unit - 1BR/1BTH", "number_of_reviews": 507, "last_review": "2025-11-15", "reviews_per_month": 2.54}
    ]
    2)
    Entrada:
    [
    {"name": "Creative Sanctuary", "number_of_reviews": 105, "last_review": "2017-08-06", "reviews_per_month": 0.52},
    {"name": "*FriendlyRoom Apt. Style -UCSF/USF - San Francisco", "number_of_reviews": 10, "last_review": "2023-07-30", "reviews_per_month": 0.07}
    ]
    ,False
    Salida:
    [
    {"name": "Creative Sanctuary", "number_of_reviews": 105, "last_review": "2017-08-06", "reviews_per_month": 0.52},
    {"name": "*FriendlyRoom Apt. Style -UCSF/USF - San Francisco", "number_of_reviews": 10, "last_review": "2023-07-30", "reviews_per_month": 0.07}
    ]
    3)
    Entrada:
    [
    {"name": "Creative Sanctuary", "number_of_reviews": 105, "last_review": "2017-08-06", "reviews_per_month": 0.52},
    {"name": "*FriendlyRoom Apt. Style -UCSF/USF - San Francisco", "number_of_reviews": 10, "last_review": "2023-07-30", "reviews_per_month": 0.07}
    ]
    ,True
    Salida:
    []
    4)
    Entrada:
    [],True
    Salida:
    []

    '''
    
    copia = alquileres.copy()
    if fue_reseñada:
        for alquiler in alquileres:
            if alquiler["last_review"].split("-")[0] != "2025": 
                copia.remove(alquiler)
    return copia

                
