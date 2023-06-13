# Дана последовательность чисел, сформировать список уникальных чисел
# [1, 2, 3, 5, 1, 2, 8 , 9, 9] = [5, 8]

lst = [1, 2, 3, 5, 1, 2, 8 , 9, 9]
lst_sorted = []

lst_sorted = [item for item in lst if lst.count(item) == 1]
print (lst_sorted)