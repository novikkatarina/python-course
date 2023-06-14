# Создайте программу для игры в ""Крестики-нолики"".

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lst[0])
print(lst[1])
print(lst[2])

def winner(list):
    for i in range(0, 3):
        if lst[i].count("X") == 3 or lst[i].count("X") == 3:  # проверка строк
            return True
        
        elif lst[0][i] == lst[1][i] == lst[2][i]: #проверка столбцов
            return True

    if lst[0][0] == lst[1][1] == lst[2][2] or lst[2][0] == lst[1][1] == lst[0][2]:
            # диагональ
            return True 
while True:
    input_prompt = 'Choose a place (you can choose from free numbers 1-9) player1 '
    while (player1:= int(input(input_prompt))) \
    not in range(1, 10) or [item for sublist in lst for item in sublist].count(player1) == 0: #ввод числа-места игроком1
            print('try again')
    # print([item for sublist in lst for item in sublist].count(player1))

    for row_i in range(3):
        for col_i in range(3):
            if lst[row_i][col_i] == int(player1):
                lst[row_i][col_i] = 'X'  #меняем на Х
    print(lst[0])
    print(lst[1])
    print(lst[2])


    if winner(lst):
        print("winner is player 1")
        exit ()


    while (player2:= int(input('Choose a place (you can choose from free numbers 1-9) player2 '))) \
    not in range(1, 10) or [item for sublist in lst for item in sublist].count(player2) == 0: #ввод числа-места игроком2
            print('try again')

    for row_i in range(3):  #меняем на O
        for col_i in range(3):
            if lst[row_i][col_i] == player2:
                lst[row_i][col_i] = 'O'
    print(lst[0])
    print(lst[1])
    print(lst[2])

    if winner(lst):
        print("winner is player 2")
        exit()

