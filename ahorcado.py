import random
import string

from palabras import palabras
from ahorcado_diagrama import vidas_diccionario_visual


def get_valid_word(lista_palabras):
    # Seleccionar una palabra al azar
    palabra = random.choice(lista_palabras)

    while '-' in lista_palabras or ' ' in palabra:
        palabra = random.choice(lista_palabras)
    
    return palabra.upper()


def ahorcado():
    print('Bienvenido al juego del ahorcado!!!')

    word = get_valid_word(palabras)

    # Conjunto, tipo de dato en especifico {'a', 'b', 'c'}
    letras_por_adivinar = set(word)
    letras_adivinadas = set()

    # retorna todo el abecedario con las letras mayusculas
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f'Te quedan {vidas} vidas y has usado estas letras: {" ".join(letras_adivinadas)}')

        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in word]

        # Mostrando estado del juego
        print(vidas_diccionario_visual[vidas])
        print(f'Palabra: {" ".join(palabra_lista)}')

        letra_usuario = input('Escoge una letra: ').upper()

        # Si la letra esta en el abecedario y no en el conjunto ingresado se añade al conjunto
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            # Si esta en la palabra, se remueve
            # si no, se elimina una vida
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f'\nTu letra {letra_usuario} no esta en la palabra')
        
        elif letra_usuario in letras_adivinadas:
            print('Ya elegiste esa letra, por favor elige una nueva')
        
        else:
            print('\nEsta letra no es valida')

    # El juego llega hasta aqui cuando se adivinan todas las letras
    # o cuando el jugador ya no tiene vidas
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f'Perdiste!!! Estas ahorcado. La palabra era: {word}')
    else:
        print('Felicidades!! Has ganado adivinaste la palabra!')


ahorcado()