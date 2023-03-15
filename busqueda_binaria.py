import random
import time


def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            # retorna el indice del target
            return i
    
    return -1


def busqueda_binaria(lista, objetivo, limite_inferior = None, limite_superior = None):
    if limite_inferior is None:
        limite_inferior = 0
    
    if limite_superior is None:
        limite_superior = len(lista) - 1
    
    if limite_superior < limite_inferior:
        return -1
    
    punto_medio = (limite_inferior + limite_superior) // 2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio - 1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio + 1, limite_superior)


if __name__=='__main__':
    # Crear una lista ordenada con 1000 numeros aleatorios
    size = 3000
    conjunto = set()

    while len(conjunto) < size:
        conjunto.add(random.randint(-3*size, 3*size))

    mi_lista_ordenada = sorted(list(conjunto)) # Sorted ordena la lista

    # Medir el tiempo de busqueda ingenua
    inicio = time.time()
    for objetivo in mi_lista_ordenada:
        busqueda_ingenua(mi_lista_ordenada, objetivo)

    fin = time.time()
    print(f'Tiempo de busqueda ingenua: {fin - inicio} segundos')

    # Medir el tiempo de busqueda binaria
    inicio = time.time()
    for objetivo in mi_lista_ordenada:
        busqueda_binaria(mi_lista_ordenada, objetivo)

    fin = time.time()
    print(f'Tiempo de busqueda binaria: {fin - inicio} segundos')