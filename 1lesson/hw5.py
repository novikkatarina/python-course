# Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

a1 = float(input ('Введите X координаты A '))
a2 = float(input ('Введите Y координаты A '))
b1 = float(input ('Введите X координаты B '))
b2 = float(input ('Введите Y координаты B '))
c = (abs(b2-a2)**2 + abs(b1-a1)**2)**0.5
print (f'-> {c}')