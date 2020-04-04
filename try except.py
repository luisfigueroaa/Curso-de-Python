try:
    answer = 10/0
    number = int(input("Ingresa un numero: "))
    print(number)
except ZeroDivisionError as err:  # colocar el tipo de error que atraparemos
    print(err)
except ValueError:
    print("Este no es un número :|")
