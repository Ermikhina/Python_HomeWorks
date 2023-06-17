# №7.1[###]. Дан текстовый csv файл. Разделитель данных #.
# Каждая строка файла представляет собой запись вида ФИО
# Например:
# Иванов#Иван#Иванович
# Петров#Петр#Петрович
# Соколов#Илья#Григорьевич
# 1) Необходимо вывести эти данные на экран построчно в виде:
# Иванов Иван Иванович
# Петров Петр Петрович
# 2) записать эти данные в список вида: [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# [*] Усложнение. Файл находится в поддиретории data текущей директории. 
# Сформировать путь к нему с использованием os.path и pathlib

# import os
# import os.path as path1
# MAIN_DIR = path1.abspath(path1.dirname(__file__))
# file_name = path1.join(MAIN_DIR, "text.csw")
# # print(f"Текущая директория: {os.getcwd()}")
# # print(MAIN_DIR)
# with open(file_name, 'r') as data:
#     for item in data:
#         print(item)


# import os
# import os.path as path1
# MAIN_DIR = path1.abspath(path1.dirname(__file__))
# file_name = path1.join(MAIN_DIR, "text.txt" )

# with open (file_name,"r") as data:
#    for item in data:
#     #   print (*item.strip().split("#"))
#     print (item.strip().split("#"))



import os
import os.path as path1
MAIN_DIR = path1.abspath(path1.dirname(__file__))
file_name = path1.join(MAIN_DIR, "text.txt" )

with open (file_name, mode = "rt", encoding = 'utf-8') as data:
    result_list = list ()
    for item in data:
    #   print (*item.strip().split("#"))
        last_name, first_name, parent = item.strip().split("#") # распаковка
        print (last_name, first_name, parent)
        list1 = [last_name, first_name, parent]
        result_list.append(list1)
print (result_list)


# import os
# import os.path as path1
# MAIN_DIR = path1.abspath(path1.dirname(__file__))
# file_name = path1.join(MAIN_DIR, "Data1.txt" )

# with open (file_name,"r") as data:
#     result_list = list ()
#     for item in data:
#     #   print (*item.strip().split("#"))
#         last_name,first_name, parent = item.strip().split("#")
#         print (last_name,first_name, parent)
#         list1 = [last_name,first_name, parent ]
#         result_list.append(list1)
# print (result_list)