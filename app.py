from xo import Game

def main() -> None:
    '''Запускаем игру'''
    
    # 1 - o
    # 2 - x

    game_map = [
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    ]
    xo = Game()
    player = 1
    print("\033c")
    xo.showGameMap()
    while True:
        try:
            check = xo.checkGame()
            if check == 1 or check == 2:
                print("Игра окончена!")
                break
            userCommand = input(f"Write your move, player#{player} ('q' for end game): ")
            if userCommand == "q":
                break
            else:
                print("\033c")
                xo.changeGameMap(int(userCommand), player)
                xo.showGameMap()
                player = 1 if player == 2 else 2
        except KeyboardInterrupt or Exception:
            break
    
    print("\nИгра окончена!")

if __name__ == '__main__':
    main()
