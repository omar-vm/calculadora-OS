from dividir import *
from multiplicacion import *
from resta import *
from sumar import *
from suma_avanzada import *

# Menú de opciones de la calculadora.
while True:
    print("===================================")
    print("\nCalculadora OS")
    print("\n======= Menú de opciones =======\n")
    print("Presiona '1' para sumar dos números")
    print("Presiona '2' para dividir")
    print("Presiona '3' si quieres sumar mas de dos números")
    print("Presiona '4' si quieres restar dos números")
    print("Presiona '5' si quieres multiplicar")
    print("Presiona 'q' si quieres salir")
    print()

    accion = input('¿Que accion deseas realizar?: ')
    accion = accion.lower()
    print()

    if accion == '1':
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print(f'\nLa suma de {a} + {b} es: ', sumar(a, b))

    elif accion == '2':
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print(f"\nLa division de {a} / {b} es: ", division(a, b))

    elif accion == '3':
        n = input("Ingresa los números que quieras sumar separados por espacio: ")
        n = list(map(float, n.split()))
        n_str = " + ".join(map(str, n))
        print(f"\nLa suma de {n_str} es: ", suma_avanzada(*n))

    elif accion == '4':
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print(f'\nLa resta de {a} - {b} es: ', resta(a, b))

    elif accion == '5':
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print(f'\nLa multiplicación de {a} * {b} es: ', multiplicacion(a, b))

    elif accion == 'q':
        break
