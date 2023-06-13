# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

import random
num = int(input('enter number: '))
lst = []
lst2 = []
for i in range(num):
    lst.append(random.randint(0, 9))
print (lst)
# for i in range (0,num):
#     if lst.count(lst[i]) == 1:
#         lst2.append(lst[i]) 

filtered = filter(lambda x: lst.count(x) == 1, lst)
lst2 = list(filtered)

print(lst2)