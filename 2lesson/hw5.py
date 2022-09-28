# Реализуйте алгоритм перемешивания списка.
import random
N = int(input('enter N: '))
#lst = [random.randint(0, N) for i in range(N)]

lst = []
for i in range(N):
    lst.append(random.randint(0, N))

print(lst)

for i in range(len(lst)):
    n = random.randint(0, N)
    tmp = lst[i]
    lst[i] = lst[n]
    lst[n] = tmp

print(lst)
