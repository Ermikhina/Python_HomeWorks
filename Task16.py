# 3.1[16]: Дан список целых чисел. Требуется вычислить, сколько раз встречается некоторое
# число X в этом списке. Пользователь вводит число X с клавиатуры. Список можно считать
# заданным. Если такого числа в списке нет - вывести -1.
# Примеры/Тесты:
# Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 3
# Output:  2
# Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 20
# Output:  -1
# Напишите алгоритм подсчета самостоятельно или воспользуйтесь методами списка.
# (*) Усложнение. При выводе результата на экран воспользуйтесь тернарным оператором.
x = int(input("Введите искомое в списке число: "))
lst = [10, 5, 7, 3, 3, 0, 5, 7, 2, 8]
n = 0
for k in range(len(lst)):
   if lst[k]==x:
     n+=1
# print(f"Число {x} встречается в списке {lst} {n} раз")
#  k = s//v + 1 if s%v!=0 else s//v     тернарный!!!
print(f"Число {x} встречается в списке {lst} {n} раз") if n>0 else print(f"Числа {x} в списке {lst} нет")