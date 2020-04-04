# Listas en más listas
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# Access
print(number_grid[2][1])

# imprimir los numeros en orden
for x in number_grid:  # para cada fila en la matriz
    print('fila: '+str(x))
    for y in x:  # para cada columna en cada fila
        print("columna: "+str(y))
