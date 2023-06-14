# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
num = int (input('number of digits '))
sum = 0
lst = []

for i in range (num):
    lst.append (random.randint (0, 10))

print (lst)
left_idx = 0
right_idx = num - 1

while left_idx <= right_idx:
    print(lst[left_idx] * lst[right_idx])
    left_idx+=1
    right_idx-=1
