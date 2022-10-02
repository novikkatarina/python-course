# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19
# n = 5.51 % 1
# print (n)

import random

# import split
num = int (input('number of digits '))
sum = 0
lst = []
frac = []
for i in range (num):
    lst.append (random.randint (0, 1000) * 0.01)
for l in lst:
    print(str(l))
    splitted = str(l).split('.')
    frac.append(int(splitted [1]) )
print(frac)
result = max(frac)-min(frac)
print (result)