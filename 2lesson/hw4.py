# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.
import random
num = int(input('enter number: '))
lst = []
for i in range(num):
    lst.append(random.randint(-1*num, num))
print(lst)
pos = input('enter positions: ').split()
mult = 1
for p in pos:
    mult *= lst[int(p)]
print(mult)
