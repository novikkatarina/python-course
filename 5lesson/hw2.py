# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

print("Rules: There is 2021 candies, you can take from 1 to 28")
print("Wins the one who's the smartest and makes the last take")
candies = 100
print(f'Candies:{candies}')
while candies > 0:
    player1 = 0
    player2 = 0
        
    while (player1 := int(input('how much do yo take, player 1? '))) not in range(1, min(candies+1, 29)):
        print('try again')
    candies -= player1
    print(f'Candies:{candies}')

    if candies <= 0:
        print("player 1 is a winner")
    if candies  > 0:
        while (player2 := int(input('how much do yo take, player 2? '))) not in range(1, min(candies+1, 29)):
            print('try again')
        candies -= player2
        print(f'Candies:{candies}')
        if candies <= 0:
            print("player 2 is a winner")
