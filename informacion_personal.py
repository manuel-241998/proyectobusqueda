informacion_personal = {
    "nombre": "manuel",
    "edad": 27,
    "ciudad": "Puyo",
    "provincia": "Pastaza",
}
print(informacion_personal)

# Clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal['ciudad'] = "Arajuno"
informacion_personal['provincia'] = "pastaza"

# Nueva clave-valor al diccionario "profesion"
informacion_personal['profesion'] = 'estudiante de tectonogia de la informacion '
print(informacion_personal)

#Verifica si la clave telefono existe
if 'telefono' in informacion_personal:
    print(informacion_personal["telefono"])
else:
    informacion_personal['telefono'] = "0993980819"
    print(informacion_personal)

# Elimina la clave "edad" del diccionario
informacion_personal.pop("edad")
print(informacion_personal)