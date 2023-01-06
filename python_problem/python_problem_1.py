import random

num = 0
    
def player_play():
    while(True):
        try:
            game_num = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
            if game_num<1 or game_num>3:
                print('1,2,3 중 하나를 입력하세요')
            else: break
        except ValueError:
            print('정수를 입력하세요')


    for i in range(game_num):
        global num
        num += 1
        printing_number('player')
        if num == 31:
            print('player win!')
            break


def computer_play():
    come_num = random.randint(1,3)

    for i in range(come_num):
        global num
        num += 1
        printing_number('computer')
        if num == 31:
            print('computer win!')
            break


def printing_number(name):
    print(name,num)

while(True):

    computer_play()
    if num == 31:
        break

    player_play()
    if num == 31:
        break

