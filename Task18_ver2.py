# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список можно считать заданным. Введенное число не обязательно
# содержится в списке.Если в списке несколько чисел "равноблизких" к заданному числу X, то выводим первое встретившееся.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10
# (*) Усложнение. Если в списке несколько чисел "равноблизких" к заданному числу X,
# выводим все числа в отсортированном виде (по возрастанию)
x = int(input("Введите искомое в списке число: "))
lst = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
delt_min = abs(lst[0]-x)
n1 = 0
n2 = 0
for k in range(len(lst)):
   if abs(lst[k]-x)<delt_min:
       delt_min=abs(lst[k]-x)
       n1 = k
   else:
    if (abs(lst[k]-x)==delt_min) and k!=n1:
       n2 = k
if abs(lst[n1]-x)==abs(lst[n2]-x):
    print(lst[n1], lst[n2]) if lst[n1]<lst[n2] else print(lst[n2], lst[n1])
else:
   if abs(lst[n1]-x)<abs(lst[n2]-x):
      print(lst[n1])
   else:
      print(lst[n2])