import random


def find_number_two(x):
    print('Bienvenido a Adivina el numero 2.')
    print(f'Selecciona un numero entre 1 y {x} para que la computadora lo adivine...')

    limite_inferior = 1
    limite_superior = x

    respuesta = ''
    while respuesta != 'c':
        # Generar prediccion
        if limite_inferior != limite_superior:
            prediction = random.randint(limite_inferior, limite_superior)
        else:
            prediction = limite_inferior # Puede ser superior tambien
        
        respuesta = input(f'Mi prediccion es {prediction}. Si es alta ingresa (A), si es baja ingresa (B) y si es correcta ingresa (C): ').lower()

        if respuesta == 'a':
            limite_superior = prediction - 1
        elif respuesta == 'b':
            limite_inferior = prediction + 1
    
    print(f'Felicidades!! La computadora adivino correctamente {prediction}!!!')


find_number_two(10)