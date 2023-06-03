# №5.2[33]. Хакер Василий получил доступ к классному журналу и хочет заменить все сво
# и минимальные оценки на максимальные.Напишите функцию, которая заменяет оценки, переданные 
# в виде списка, но наоборот: все максимальные – на минимальные.
# Функция должна возвращать новый список оценок
# Примечание: Обратите внимание на side effects функции.
# Примеры/Тесты:
# <function_name>([1, 3, 3, 3, 4, 2, 5, 5, 2]) -> [1, 3, 3, 3, 4, 2, 1, 1, 2]
# [*] Усложненение: Если ни одна оценка не была заменена, функция должна вернуть None
# Примеры/Тесты:
# <function_name>([3, 3, 3, 3, 3, 3, 3, 3, 3]) -> None
# [**] Усложненение: Добавьте параметр в функцию, который определит как будут заменены оценки:
# Друзьям минимальные на максимальные, Врагам - наоборот.
# Примеры/Тесты:
# grades = [1, 3, 3, 3, 4, 2, 5, 5, 2]
# <function_name>(grades, "friend") -> [5, 3, 3, 3, 4, 2, 5, 5, 2]
# <function_name>(grades, "enemy") -> [1, 3, 3, 3, 4, 2, 1, 1, 2]
def change_grade(grades):
    max_grade = max(grades)
    min_grade = min(grades)
    if max_grade == min_grade:
        return None
    for i in range(len(grades)):
        if grades[i] == max_grade:
            grades[i] = min_grade
    return grades
gr = [1, 3, 3, 3, 4, 2, 5, 5, 2]
print(change_grade(gr))


# def change_grade(grades):
#     max_grade = max(grades)
#     min_grade = min(grades)
#     print(max_grade, min_grade)
#     for i in range(len(grades)):
#         if grades[i] == max_grade:
#             grades[i] = min_grade
#     return grades
# gr = [1, 3, 3, 3, 4, 2, 5, 5, 2]
# print(change_grade(gr))