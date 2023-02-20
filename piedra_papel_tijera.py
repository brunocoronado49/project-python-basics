import random


def juego():
    print('Bienvenido al juego de piedra, papel o tijera!')
    usuario = input('Elige una opcion: "pi" para piedra, "pa" para papel o "ti" para tijeras: \n').lower()
    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return 'Empate!!!'
    
    if jugador_ganador(usuario, computadora):
        return 'Ganaste!!!'
    
    return f'Perdiste!!! La computadora eligio {computadora}!'


def jugador_ganador(jugador, oponente):
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(juego())