# Напишите программу, которая будет преобразовывать десятичное число в двоичное 
# (без встроенных функций).

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('insert number '))
list = []
def from_decimal_to_binar(number):
    if number == 0:
        print (0)
        return
    while number > 0:
        number_decimal = number % 2
        number = (number - number_decimal) / 2
        list.insert(0, str(int(number_decimal)))
    print (''.join(list))   
from_decimal_to_binar(num)