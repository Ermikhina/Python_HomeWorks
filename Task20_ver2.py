# 3.3[20]: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, 
# что на вход подается только одно слово, которое содержит либо только английские, либо только 
# русские буквы и заранее известно какой алфавит надо использовать.

# Примеры/Тесты:
# Input:   ноутбук
# Output:  12

# Input:   notebook
# Output:  14
# (*) Примечание.
# Подумайте о том какие структуры данных здесь наиболее удобно использовать, чтобы просто проверять 
# в какую группу попадает буква, а также просто накапливать сумму очков.

let_lat = [['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], ['D', 'G'],
['B', 'C', 'M', 'P'], ['F', 'H', 'V', 'W', 'Y'], ['K'],
['J', 'X'], ['Q', 'Z']]
let_cost  = [1, 2, 3, 4, 5, 8, 10]

word_cost = 0
word = "notebook"
for char in word.upper():
    for i in range(len(let_lat)):
        if char in let_lat[i]:
            word_cost += let_cost[i]
            break
print(f"Стоимость слова: {word_cost}")


# С 41-й минуты!!! Семинар 4