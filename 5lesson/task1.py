# Найти недостающий элемент в последовательности

def file_reading(x):
    with open(f'{x}', 'r') as file:
        y = file.read()
    return y
def search_propysk(x):
    for i in range(len(x) - 1):
        if x[i] + 1 != x[i+1]:
            return x[i] + 1

list_numbers = file_reading('file_5lrsson_1task.txt').split()
print(list_numbers)
list_numbers = list(map(int, list_numbers)) #перевод из строк в массив чисел, каждый элемент (строка) перевел в int
num = search_propysk(list_numbers)
print(num)