def buscar_valor(busqueda, valor):
    for i in range(len(busqueda)):
        for j in range(len(busqueda[i])):
            if busqueda[i][j] == valor:
                return f"El valor {valor} se encontró en la posición ({i}, {j})."
    return f"El valor {valor} no se encontró en la matriz."


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

valor_buscar = 5

resultado_busqueda = buscar_valor(matriz, valor_buscar)

print(resultado_busqueda)

