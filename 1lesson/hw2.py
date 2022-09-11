# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = int(input ('Введите X: '))
Y = int(input ('Введите Y: '))
Z = int(input ('Введите Z: '))
if (not(X and Y and Z))==(not X or not Y or not Z):
    print('true')
else:
    print('false')