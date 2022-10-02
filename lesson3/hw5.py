# Задайте число. Составьте список чисел Фибоначчи, в том числе для
# отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
t = int(input('insert number '))
list = [0, 1]
n = 0
k = 1
for i in range(t-1):
    l = list[n] + list[k]
    list.append(l)
    n += 1
    k += 1
print(list)
list2 = list[:]
for i in range(t):
    if i%2 == 0:
        list.insert(0,(list2[i+1]) )
    else:
        list.insert(0,( -list2[i+1]) )  
print(list)
