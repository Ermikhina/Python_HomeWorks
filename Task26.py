# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. 
# Разрешается использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

def step(a, b):
    if b==0:
        return 1
    elif b<0:
        return step(a, b+1)/a
    return step(a, b-1)*a
    
a = int(input("Введите основание a: "))
b = int(input("Введите степень b: "))
print(f"{a} в степени {b} равно {step(a, b)}")
