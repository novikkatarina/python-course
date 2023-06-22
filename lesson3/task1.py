# 3. Задайте список, напишите программу, которая определит, присутствует ли в данном списке строк
#  некоторое число
# "654hn6"
#  "7"

# mylist = ['ebwy67','vnsik46','jgnkd7h']
# n = 7
# for i in mylist:
#     if i.find('7') >= 0: #find ищет позицию в строке, если он не находит, то позиция -1
#         print (i)
#     else:
#         print ('none')

# 2.Найти второе вхождение элемента

# mylist = ['qwe', 'ehjk', 'uetgij', 'qwe', 'qwefhn']
# index = 0

# for i in range (len(mylist)):
#     if mylist[i].find('qwe') >= 0:
#         index += 1
#         if index == 2:
#             print(i)
# if index < 2:
#         print ("none")

# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного
# генератора псевдослучайных чисел

from time import sleep, time
num = int(input('number of digits '))
numbers = []
for i in range(num):
    sec = time()
    sec2 = (sec * 1000000) % 100
    sleep(0.0001 * sec2)
    sec_without_decimal = str(sec2).split('.')
    numbers.append (sec_without_decimal[0])
print(numbers)
