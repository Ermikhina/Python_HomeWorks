# 1.1[2]. Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод
# Например для числа 145 сумма цифр будет 10: 1 + 4 + 5

# Примеры/Тесты:
# 123 >>> Сумма чисел числа 123 равна 6
# 100 >>> Сумма чисел числа 100 равна 1
# (*) Усложнение. Решите для числа произвольной разрядности: произвольное количество цифр в числе.

# (**) Усложнение. Для числа произвольной разрядности добавить в вывод строку с числами, например так:

# 13579 >>> Сумма чисел числа 13579 равна 25(1 + 3 + 5 + 7 + 9)
# Совет: Для этого используйте конкатенацию строк и срезы
# https://disk.yandex.ru/d/F1fvMUbtxEx8UA
# Задача 2: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
number = int(input("Введите 3-хзначное число: "))
sumdig = number//100 + number//10%10+number%10
print(f"Сумма цифр числа {number} = {sumdig}")