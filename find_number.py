import random


def find_number(x):
    print('Bienvenido a Adivina el numero.')
    print('Tu meta es adivinar el numero generado por la computadora')

    numero_random = random.randint(1, x)
    prediction = 0

    while prediction != numero_random:
        prediction = int(input(f'Ingresa un valor entre el 1 y {x}: '))

        if prediction < numero_random:
            print('Intenta otra vez. Este numero es menor.')
        elif prediction > numero_random:
            print('Intenta otra vez. Este numero es mayor.')

    print(f'Felicidades!!! Adivinaste el numero {numero_random} correctamente.')


find_number(10)