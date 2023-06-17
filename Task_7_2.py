# №7.2[###]. Продолжение предыдущей задачи 
# Данные в списке [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# необходимо  преобразовать к виду:
# Иванов И.И.
# Петров П.П.

# Полученные строки записать в новый файл. Файл должен находиться в поддиретории rezults.
# [*] Усложнение. Данные необходимо записать в два разных файла:
#     В первый - в виде Иванов И.И.
#     Во второй - в виде Иванов-И-И

import os
import os.path as path1
MAIN_DIR = path1.abspath(path1.dirname(__file__))
file_name = path1.join(MAIN_DIR, "text.txt" )

with open (file_name,mode = "rt", encoding = 'utf-8') as data:
    result_list = list ()
    for item in data:
    #   print (*item.strip().split("#"))
        last_name, first_name, parent = item.strip().split("#")
        # print (last_name, first_name, parent)
        list1 = [last_name, first_name, parent ]
        result_list.append(list1)
# print (result_list)


# file_name2 = path1.join(MAIN_DIR, "Results", "Names.txt")
file_name2 = path1.join(MAIN_DIR, "Names.txt")
with open(file_name2, mode = "wt", encoding="utf-8") as result_file:
    for last_name,first_lit, parent in result_list:
        str1 = f"{last_name} {first_lit[0]}.{parent[0]}.\n"
        result_file.write(str1)

file_name3 = path1.join(MAIN_DIR, "Names2.txt")
with open(file_name3, mode = "wt", encoding="utf-8") as result_file:
    for last_name, first_lit, parent in result_list:
        str1 = f"{last_name} {first_lit[0]}-{parent[0]}\n"
        result_file.write(str1)