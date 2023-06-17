# №8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
# Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller

# human = ["name", "sec_name", phone_number, "description"]
# phone_dir = {1: ["name", "surname", phone_number, "description"], 2: ["name", "sec_name", phone_number, "description"]}
# idc - счётчик ключей

def Input_Users()->list:
    user = []
    user.append(input("Введите имя: "))
    user.append(input("Введите фамилию: "))
    user.append(input("Введите номер телефона: "))
    user.append(input("Введите описание: "))
    return user
key_count =0
phone_dir = dict()
def create( phone_dir_local: dict, idc: int,  user:list)->dict:
    idc += 1
    phone_dir_local[idc] = user
    return phone_dir_local, idc

user1 = ["second_name1","first_name1","phone1","discription1"]
user2 = ["second_name2","first_name2","phone2","discription2"]

phone_dir, key_count=create(phone_dir,key_count,user1)
phone_dir, key_count=create(phone_dir,key_count,user2)
print(phone_dir)

# def menu():
#     num = 100
#     while num != 0:
#         num = int(f"Выберите операцию: 1 - ввести пользователя, 2 - распечатать справочник, 0 - выйти")
#         if num == 1:


# user1 = ["second_name1","first_name1","phone1","discription1"]
# user2 = ["second_name2","first_name2","phone2","discription2"]

# phone_dir, key_count=create(phone_dir,key_count,user1)
# phone_dir, key_count=create(phone_dir,key_count,user2)
# print(phone_dir)

def menu ():
    print("Введите 1, если хотите ввести пользователя ")
    print("Введите 2, если хотите распечатать справочник ")
    key_count =0
    phone_dir = dict()
    while True:
        num = int(input("Выберите операцию "))
        if num == 0:
            break
        if (num ==1):
           user = Input_Users()
           phone_dir, key_count = create(phone_dir,key_count,user)
        if num == 2:
            print (phone_dir)
        if num == 3:
            file_name = input("Введите имя файла: ")

 def export_phone_dir(phone_dir:dict, file_name:str):


import os
import os.path as path1
MAIN_DIR = path1.abspath(path1.dirname(__file__))
file_name = path1.join(MAIN_DIR, "text.txt" )
menu ()



{1: ['Иванов',   'Иван',  '+7(xxx)xxx-xx-xx', 'desription_Иванов'], 
2: ['Петров',   'Петр',  '+7(---)xxx-xx-xx', 'desription_Петров'], 
3: ['Соколов',  'Илья',  '+7(---)---------', 'desription_Соколов'], 
4: ['Павельев', 'Андрей','+7(***)***-**-**', 'desription_Павельев'], 
5: ['Пешехов',  'Антон', '+7++++++++++',     'desription_Пешехов'], 
6: ['Сааков',   'Илья',  '+7(+++)+++-++-++', 'desription_Сааков'], 
}