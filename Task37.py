# №5.4[37] Напишите функцию, которая принимает натуральное число n, в теле функции считывает (input) 
# последовательность из n элементов и возвращает эту последовательность в виде строки в обратном порядке
# Примеры/Тесты:
# <function_name>(5) 1 2 3 4 5 -> '5 4 3 2 1'
# <function_name>(3) 8 7 9 -> '9 7 8'
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).


# def form_string(n:int) -> str:
#     num = input()
#     if n==1:
#         return digit
#     return form_string(n-1) + digit
    
# print(form_string(5))



def sequence(n: int) -> str:
    digit = input()
    if n == 1:
       return digit + ' '
    return sequence(n-1) + digit + ' '

print(sequence(5))
