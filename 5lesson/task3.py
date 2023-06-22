# Дан список чисел. Создайте список чисел, в который попадают чтсла, описываемые в возрастающую 
# последовательность. Порядок элементов менять нельзя.

# [1, 3, 5, 4, 3, 6, 7] - [1, 3, 5, 6, 7]

list = [1, 3, 5, 4, 3, 6, 7]
list_increasing = [list[0]]
max = list[0]
for i in range (len(list)-1):
    if list [i+1] > max:
        max = list [i+1]
        list_increasing.append(list[i+1])
print (list_increasing)
