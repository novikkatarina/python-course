# Напишите программу,удаляющую все слова, содержащие "абв"

my_string = 'Мы  неабв любим Питон иабв'
sub = 'абв'


my_string = 'Мы неабв очень любим Питон иабв Джавабв'.split()
print(my_string)
result_list = []
for i in range(len(my_string)):
    if 'абв' not in my_string[i]:
        result_list.append(my_string[i])
print(result_list)
result_string = (' ').join(result_list)
print (result_string)