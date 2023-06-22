# Найти недостающий элемент в последовательности


def file_reading(x):
    filename = f'{x}'
    access_mode = 'r'
    # open is system function, context manager
    with open(filename, access_mode) as file:
        y = file.read()
    return y


def search_propysk(x):
    # for i in range(len(x) - 1):
    #     if x[i] + 1 != x[i+1]:
    #         return x[i] + 1
    for i, ch in enumerate(x):
        if ch + 1 != x[i + 1]:
            return ch + 1


list_numbers = file_reading('file_5lrsson_1task.txt').split()
print(list_numbers)
# lambda x: int(x)
m = map(int, list_numbers) # map выполняет функцию в первом аргументе для кажд элемента во втором аргументе
list_numbers = list(m)  # перевод из строк в массив чисел, каждый элемент (строка) перевел в int
num = search_propysk(list_numbers)
print(num)
