# Напишите программу вычисления арифметического выржаения заданного строкой
# Используйте * / + - приоритет стандартный

# 2+2 = 4
# 1+2*3 = 7

str = "2 * ((3 + 1) * 2 + 4)"

str = str.split()
for i in range(len(str)):
    if str[i].isdigit():
        str[i] = int(str[i])

op_1 = {'+': lambda x, y: x + y,
        '-': lambda x, y: x - y}
op_2 = {'*': lambda x, y: x * y,
        '/': lambda x, y: x / y}

index = 0

print(str)

while '*' in str or '/' in str:
    if str[index] in op_2:
        temp = op_2[str[index]](str[index - 1], str[index + 1])
        del str[index - 1:index + 2]
        str.insert(index - 1, temp)        
        index = 0
    else:
        index += 1

index = 0

while '+' in str or '-' in str:
    if str[index] in op_1:
        temp = op_1[str[index]](str[index - 1], str[index+1])
        del str[index - 1:index + 2]
        str.insert(index - 1, temp)
        index = 0
    else:
        index += 1

print(str)
