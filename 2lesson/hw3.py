# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

number = int(input('enter number: '))
sum = 0
for k in range(1, number + 1):
    sum += (1 + 1/k)**k
print(sum)
