# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, 
# в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит 
# число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# Ввод: 
# 7 
# 3 1 3 4 2 4 12  (каждое число вводится с новой строки)
# 6
# 4 15 43 1 15 1 
# Вывод: 3 3 2 12

n1 = int(input("Введите кол-во элементов 1-го массива: "))
arr1 = []
for i in range (n1):
    arr1.append(int(input(f"Введите {i+1}-й элемент 1-го массива: ")))
print(arr1)
n2 = int(input("Введите кол-во элементов 2-го массива: "))
arr2 = []
for i in range (n2):
    arr2.append(int(input(f"Введите {i+1}-й элемент 2-го массива: ")))
print(arr2)
for i in range (n1):
    if arr1[i] not in arr2:
        print(arr1[i])


        def defference_list(list1: list, list2: list) -> list:
    set_list2 = set(list2)
    new_list = []
    for item in list1:
        if item not in set_list2:
            new_list.append(item)
    return new_list


# Сравнение времени выполнения алгоритма с множеством и списком:

from time import perf_counter
from random import randint

def difference_set(list1: list, list2: list) -> list:
    t1 = perf_counter()
    set_list2 = set(list2)
    res = [item for item in list1 if item not in set_list2]
    t2 = perf_counter()
    return t2 - t1

def difference_list(list1: list, list2: list) -> list:
    t1 = perf_counter()
    res = [item for item in list1 if item not in list2]
    t2 = perf_counter()
    return t2 - t1

n = 10000
lst1 = [randint(0, n) for i in range(n)]
lst2 = [randint(0, n) for i in range(n)]

print(f" SET: {difference_set(lst1, lst2):3e}")
print(f"LIST: {difference_list(lst1, lst2):3e}")