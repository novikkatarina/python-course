# Вычислить число c заданной точностью d
# Пример:

# при $d = 0.001, π = 3.141
import math
d = int(input('insert accuracy '))

p = math.pi
print(f'{p:.{d}f}'.format(round(p, ))) 
