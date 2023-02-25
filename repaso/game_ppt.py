import random


def game_ppt():
    print('===========================================================')
    print('====   Bienvenido al juego de Piedra, papel o tijera   ====')
    print('===========================================================')

    usuario = input(
        'Elige una opcion: "piedra", "papel" o "tijera" y juega contra la computadora: ')
    computadora = random.choice(["piedra", "papel", "tijera"])

    if usuario == computadora:
        return 'Es un empate!!!'

    if juego(usuario, computadora):
        return 'Felicidades has ganado la partida!!!'
    
    return f'Buuuu!!! Perdiste la computadora saco {computadora}'


def juego(jugador, oponente):
    if ((jugador == 'papel' and oponente == 'piedra')
    or (jugador == 'piedra' and oponente == 'tijera')
    or (jugador == 'tijera' and oponente == 'papel')):
        return True
    else:
        return False


print(game_ppt())