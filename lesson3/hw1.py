# # Задайте список из нескольких чисел. Напишите программу, 
# # которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# # Пример:

# # - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

import random

num = int (input('number of digits '))

# sum = 0
# lst = []

# for i in range (num):
#     lst.append (random.randint (0, 10))

# print (lst)

# for i in range(num):
#     if i % 2 != 0:
#         sum += lst[i]
# print (sum)

lst = [random.randint (0, 10) for i in range(num)]

print (lst)

filtered = filter(lambda pair: pair[0] % 2 != 0, enumerate(lst))
mapped = map(lambda pair: pair[1], filtered)

print(sum(list(mapped)))