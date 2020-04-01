num1 = float(input('Ingresa el primer número: '))
op = input('Ingrese el simbolo de la operación: ')
num2 = float(input('Ingresa el segundo número: '))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print('Operador no válido')
