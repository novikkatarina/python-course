# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
s1 = ''
s2 = ''
with open('file2.txt','r') as f:
    s1 = f.read()

with open('file3.txt','r') as f:
    s2 = f.read()

s1 = s1[:-4] #удалить = 0
s2 = s2[:-4]

l1 = s1.split(' + ')
l2 = s2.split(' + ')
# print(l1)
# print(l2)

def contains_power_of(lst, p):
    for l in lst:
        if p == 0:
            if l.count('x') == 0: #если нет х - значит х в нулевой степени - число
                return l
        elif p == 1:
            if l.count('^') == 0 and l.count('x') == 1: #x^1
                return l
        else:
            if f'^{p}' in l:
                return l
    return ''

res = []

for i in range(10):
    r = 0
    c1 = contains_power_of(l1, i)
    if c1 != '':
        k1 = int(c1.split('*')[0]) #берем число
        r += k1
    c2 = contains_power_of(l2, i)
    if c2 != '':
        k2 = int(c2.split('*')[0])
        r += k2
    
    if r != 0:
        if i == 0:
            res.append(f'{r}')
        elif i == 1:
            res.append(f'{r}*x')
        else:
            res.append(f'{r}*x^{i}')
res = res[::-1] #в обратном порядке
# print(res)
res_s = (' + ').join(res)
res_s += ' = 0'
print(res_s)

with open('file4.txt','w') as f:
    f.write(res_s)
