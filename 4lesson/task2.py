# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#     1) с помощью математических формул нахождения корней квадратного уравнения
#     *2) с помощью дополнительных библиотек Python

a = float(input ('enter a: '))
b = float(input ('enter b: '))
c = float(input ('enter c: '))
print (f'{a}*x^2 + {b}*x + {c} = 0')
disk = 0
def discriminant(a, b, c):
    disk = b * b - 4 * a * c
    return disk

if (disk<0):
    print ('no solution')
elif (disk == 0):
    x = -b/2*a
    print(f'x= {x}')
elif (disk>0):
    x1 = (-b + d**0.5)/2*a
    x2 = (-b - d**0.5)/2*a
    print(f'x1 = {x1}, x2 = {x2}')



# import math

