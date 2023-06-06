# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве  Далее записаны N чисел — элементы 
# массива. Массивсостоит из целых чисел.
# Ввод:
# 5
# 1 2 3 4 5   (каждое число вводится с новой строки)
# Вывод: 
# 0
# Ввод:
# 5
# 1 5 1 5 1
# Вывод:
# 2

def neibours (list1: list) -> list:
    result_list = list()
    for idx in range(len(list1)-1):
        if list1[idx-1]<list1[idx]>list1[idx+1]:
            result_list.append(list1[idx])
    idx =  len(list1)-1      
    if list1[idx-1]<list1[idx] and list1[0]<list1[idx]:
            result_list.append(list1[idx])    
    return result_list

print(neibours([1, 3, 3, 3, 5])) 
print(neibours([1, 5, 1, 6, 1]))
print(neibours([7, 5, 1, 6, 8]))
print(neibours([8, 1, 5, 4, 5]))


