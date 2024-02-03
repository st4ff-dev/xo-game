from xo import Game

def main() -> None:
    '''Запускаем игру'''
    
    # 1 - Нолик
    # 2 - Крестик

    game_map = [
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    ]
    xo = Game()
    state = 1

    while True:
        try:
            check = xo.checkGame()
            if check == 1 or check == 2:
                print("Игра окончена!")
                break
            elif state == 1:
                userCommand = input("Введите ваш ход, пользователь 1 (q для выхода): ")
                if userCommand == "q":
                    break
                else:
                    xo.changeGameMap(int(userCommand), state)
                    xo.showGameMap()
                    state = 2
            elif state == 2:
                userCommand = input("Введите ваш ход, пользователь 2 (q для выхода): ")
                if userCommand == "q":
                    break
                else:
                    xo.changeGameMap(int(userCommand), state)
                    xo.showGameMap()
                    state = 1
        except KeyboardInterrupt or Exception:
            break
    
    print("\nИгра окончена!")

def checkGame():
    pass

if __name__ == '__main__':
    main()