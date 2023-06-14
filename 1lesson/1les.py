# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90


num_1 = int(input ('Введите 1 число: '))
num_2 = int(input ('Введите 2 число: '))
num_3 = int(input ('Введите 3 число: '))
num_4 = int(input ('Введите 4 число: '))
num_5 = int(input ('Введите 5 число: '))
max = num_1
if (num_2 > max):
    max = num_2
if (num_3 > max):
    max = num_3
if (num_4 > max):
    max = num_4
if (num_5 > max):
    max = num_5
print (max)

# range(5) -> [0, 1, 2, 3, 4]
# range(5, 16) -> [5, 6, 7 ..., 13, 14, 15]
# range(1, 11, 2) -> [1, 3, 5, 7, 9]

# my_list = []
# for i in range(5):
#     num = int(input('--> '))
#     my_list.append(num)
# print(my_list)


# my_list = [3, 5, 1, 2, 8]
# maxx = my_list[0]
# maxx_i = 0
# for i in range(1, len(my_list)):
#     if my_list[i] > maxx:
#         maxx = my_list[i]
#         maxx_i = i

# print(maxx, maxx_i)
