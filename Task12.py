# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3
# Примечание.
# Здесь нужно составить два уравнения. Которые приведут к квадратному уравнению.
# Кто не помнит, как решать квадратное уравнение - посмотрите в сети. Обойдите дополнительной проверкой
# возможность комплексных решений. Можно игнорировать то, что получатся рациональные решения вместо натуральных.
# Для вычисления квадратного корня используйте возведение в степень 0.5 или (*) 
# Усложнение. найдите самостоятельно в сети какая функция стандартной библиотеки вычисляет 
# квадратный корень и как до нее добраться.

sum = int (input("Введите сумму чисел x и y: "))
com = int (input("Введите произведение чисел x и y: "))
import math
d = sum*sum-4*com
if d==0:
    x1 = (sum + math.sqrt(d))/2
    y1 = sum - x1
    print(f"Решение: x = {x1}, y = {y1}")
elif d>0:
    x1 = (sum + math.sqrt(d))/2
    x2 = (sum - math.sqrt(d))/2
    y1 = sum - x1
    y2 = sum - x2
    print(f"Решение 1: x = {x1}, y = {y1}")
    print(f"Решение 2: x = {x2}, y = {y2}")
else:
    print ("Решений нет")