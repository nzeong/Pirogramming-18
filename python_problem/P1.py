
num = 0
game_num = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
    
    while(True):
        try:
            game_num = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : '))
            if game_num<1 or game_num>3:
                print('1,2,3 중 하나를 입력하세요')
            else: break
        except ValueError:
            print('정수를 입력하세요')
