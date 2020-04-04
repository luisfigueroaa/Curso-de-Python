# r=read - w:write - a:add - r+:read and write
datos_personales = open("texto.txt", "r")

for dato in datos_personales.readlines():
    print(dato)


# print('Readable:')
# print(datos_personales.readable())  # return a booleable value - true or false
# print('Read:')
# print(datos_personales.read())
# print('ReadLine:')
# print(datos_personales.readline())
# print(datos_personales.readline())
# print(datos_personales.readlines()[1]) #se puede poner el vector con la posicion del vector que queremos leer


datos_personales.close()
