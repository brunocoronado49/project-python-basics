import time
import random


def ingenue_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
        
        return -1


def binary_search(list, target, first_limit = None, last_limit = None):
    if first_limit is None:
        first_limit = 0

    if last_limit is None:
        last_limit = 0

    if last_limit < first_limit:
        return -1

    middle_point = (first_limit + last_limit) // 2

    if list[middle_point] == target:
        return middle_point
    elif middle_point < list[middle_point]:
        return binary_search(list, target, first_limit, middle_point - 1)
    else:
        return binary_search(list, target, middle_point + 1, last_limit)


if __name__ == '__main__':
    size = 35000
    conjunte = set()

    while len(conjunte) < size:
        conjunte.add(random.randint(-3*size, 3*size))

    my_order_list = sorted(list(conjunte))

    # Ingenue search
    inicio = time.time()
    for target in my_order_list:
        ingenue_search(my_order_list, target)
    end = time.time()
    print(f'Time ingenue search: {end - inicio} seconds.')

    # Binary search
    inicio = time.time()
    for target in my_order_list:
        binary_search(my_order_list, target)
    end = time.time()
    print(f'Time binary search: {end - inicio} seconds.')
