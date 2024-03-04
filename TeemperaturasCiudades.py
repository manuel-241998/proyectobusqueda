# Mostrar las temperaturas de las ciudades
temperatures = [
    # Ciudad: Quito
    [
        {"city": "Quito"},
        [  # Semana 1
            {"day": "Monday", "temp": 74},
            {"day": "Tuesday", "temp": 16},
            {"day": "Wednesday", "temp": 23},
            {"day": "Thursday", "temp": 44},
            {"day": "Friday", "temp": 20},
            {"day": "Saturday", "temp": 63},
            {"day": "Sunday", "temp": 68},
        ],
        [  # Semana 2
            {"day": "Monday", "temp": 23},
            {"day": "Tuesday", "temp": 69},
            {"day": "Wednesday", "temp": 80},
            {"day": "Thursday", "temp": 80},
            {"day": "Friday", "temp": 45},
            {"day": "Saturday", "temp": 25},
            {"day": "Sunday", "temp": 78},
        ],
        [  # semana 3
            {"day": "Monday", "temp": 27},
            {"day": "Tuesday", "temp": 48},
            {"day": "Wednesday", "temp": 35},
            {"day": "Thursday", "temp": 56},
            {"day": "Friday", "temp": 87},
            {"day": "Saturday", "temp": 98},
            {"day": "Sunday", "temp": 64},
        ],
        [   # semana 4
             {"day": "Monday", "temp": 56},
             {"day": "Tuesday", "temp": 34},
             {"day": "Wednesday", "temp": 65},
             {"day": "Thursday", "temp": 65},
             {"day": "Friday", "temp": 78},
             {"day": "Saturday", "temp": 85},
             {"day": "Sunday", "temp": 62},
        ],
    ],
    [
        {"city": "Lago Agrio"},
        [   # semana 1
             {"day": "Monday", "temp": 44},
             {"day": "Tuesday", "temp": 43},
             {"day": "Wednesday", "temp": 19},
             {"day": "Thursday", "temp": 26},
             {"day": "Friday", "temp": 71},
             {"day": "Saturday", "temp": 88},
             {"day": "Sunday", "temp": 54},
        ],
        [   # semana 2
             {"day": "Monday", "temp": 56},
             {"day": "Tuesday", "temp": 22},
             {"day": "Wednesday", "temp": 27},
             {"day": "Thursday", "temp": 35},
             {"day": "Friday", "temp": 18},
             {"day": "Saturday", "temp": 67},
             {"day": "Sunday", "temp": 98},
        ],
        [   # semana 3
             {"day": "Monday", "temp": 67},
             {"day": "Tuesday", "temp": 56},
             {"day": "Wednesday", "temp": 42},
             {"day": "Thursday", "temp": 47},
             {"day": "Friday", "temp": 49},
             {"day": "Saturday", "temp": 56},
             {"day": "Sunday", "temp": 55},
        ],
        [   # semana 4
             {"day": "Monday", "temp": 78},
             {"day": "Tuesday", "temp": 72},
             {"day": "Wednesday", "temp": 73},
             {"day": "Thursday", "temp": 37},
             {"day": "Friday", "temp": 35},
             {"day": "Saturday", "temp": 69},
             {"day": "Sunday", "temp": 67},
        ],
    ],
    [
        {"city": "Cuenca"},
        [   # semana 1
             {"day": "Monday", "temp": 25},
             {"day": "Tuesday", "temp": 24},
             {"day": "Wednesday", "temp": 19},
             {"day": "Thursday", "temp": 56},
             {"day": "Friday", "temp": 87},
             {"day": "Saturday", "temp": 98},
             {"day": "Sunday", "temp": 78},
        ],
        [   # semana 2
             {"day": "Monday", "temp": 65},
             {"day": "Tuesday", "temp": 20},
             {"day": "Wednesday", "temp": 45},
             {"day": "Thursday", "temp": 75},
             {"day": "Friday", "temp": 55},
             {"day": "Saturday", "temp": 67},
             {"day": "Sunday", "temp": 89},
        ],
        [   # semana 3
             {"day": "Monday", "temp": 65},
             {"day": "Tuesday", "temp": 92},
             {"day": "Wednesday", "temp": 55},
             {"day": "Thursday", "temp": 34},
             {"day": "Friday", "temp": 33},
             {"day": "Saturday", "temp": 23},
             {"day": "Sunday", "temp": 65},
        ],
        [   # semana 4
             {"day": "Monday", "temp": 42},
             {"day": "Tuesday", "temp": 46},
             {"day": "Wednesday", "temp": 54},
             {"day": "Thursday", "temp": 94},
             {"day": "Friday", "temp": 72},
             {"day": "Saturday", "temp": 25},
             {"day": "Sunday", "temp": 23},
        ],
    ]
]
# Obtener las temperaturas para la ciudad seleccionada
no_ciudad = 2
for ciudad_temps in temperatures:
    no_ciudad += 1
    city_name = ciudad_temps[0]["city"]
    print(f"CIUDAD No. {no_ciudad}: {city_name}")
    no_semana = 0
    for semana in ciudad_temps[1:]:
        no_semana += 1
        suma = 0
        for day in semana:
            suma += day["temp"]
        promedio = round(suma / len(semana), 2)
        print(f"El promedio semana No. {no_semana} es: {promedio}")