# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input('enter k: '))
s = ''
for i in range(k + 1):
    k -= 1
    a = random.randint(0,100)
    if a == 0:
        continue

    if i < k + 1:
        s += f'{a}*x^{k} + '
    elif k == 1:
        s += f'{a}*x + '
    elif k == 0:
        s += f'{a} '

s += '= 0'
print(s)

with open('file.txt','w') as f:
    f.write(s)

