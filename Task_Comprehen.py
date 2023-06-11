# Генерация списка чисел от 1 до 100
list_1=[i for i in range(1, 101)]   # List Comprehension
print(list_1)

# Генерация списка только чётных чисел от 1 до 100
list_1=[i for i in range(1, 101) if i % 2 == 0]   # List Comprehension
print(list_1)

# Генерация списка кортежей только чётных чисел от 1 до 100
list_1=[(i, i) for i in range(1, 101) if i % 2 == 0]   # List Comprehension
print(list_1)

# Генерация списка чётных чисел по формуле i*2 от 1 до 10
list_1=[i*2 for i in range(10) if i % 2 == 0]   # List Comprehension
print(list_1)
