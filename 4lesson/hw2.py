# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

number = int(input('number '))
i = 2
l = []

def factors_of_number(num):
    global i
    if num <= 1:
        return
    if (num % i == 0):
        num/= i
        l.append(i)
        factors_of_number(num)
    else:
        i+= 1
        factors_of_number(num)

factors_of_number(number)
print(l)