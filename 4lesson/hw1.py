# Вычислить число c заданной точностью d
# Пример:

# при $d = 0.001, π = 3.141
import math
from decimal import Decimal
d = input('insert accuracy ')

p = math.pi
# p.toFixed(d)
# p = p.quantize(Decimal(int('d')))
# print(f'{p:.{d}f}'.format(round(p, )))
precision = len(d.split('.')[1])
print(f'{p:.{precision}f}')