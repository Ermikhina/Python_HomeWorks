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
def input_data()->list:
    human = []
    human.append(input("Введите имя: "))
    human.append(input("Введите фамилию: "))
    human.append(input("Введите номер телефона: "))
    human.append(input("Введите описание: "))
    return human

# print(input_data())

def create(phone_dir:dict, human:list)->dict:
    idc += 1
    phone_dir[idc] = human
    return phone_dir, key_count

key_count = 0
phone_dir = dict()
human = ["name", "sec_name", phone_number, "description"]
human = ["name", "sec_name", phone_number, "description"]


    # user=["ferstname","secondname","phone","discription"]
# dictionary = {1:["ferstname","secondname","phone","discription"],2:["ferstname","secondname","phone","discription"]}

# def Input_Users()->list:
#     user=[]
#     user.append(input("Input ferst name "))
#     user.append(input("Input second name "))
#     user.append(input("Input phone "))
#     user.append(input("Input discription "))
    
#     return user
# print(Input_Users())
# # def create( user:list)->dict:

# pop()

# pop(idc, default)- ошибки не будет