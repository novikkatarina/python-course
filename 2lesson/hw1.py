# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

string = input('enter number ')

res = 0
for char in string:
    if char.isnumeric():  # python check if character is number
        res += int(char)

print(res)
