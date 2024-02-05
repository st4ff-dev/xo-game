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
                xo.changeGameMap(int(userCommand), player)
                xo.showGameMap()
                player = 1 if player == 2 else 2
        except KeyboardInterrupt or Exception:
            break
    
    print("\nИгра окончена!")

def pushGame(player: int, xo: Game) -> None:
    userCommand = input(f"Write your move, player#{player} ('q' for end game): ")
    if userCommand == "q":
        return 0
    else:
        xo.changeGameMap(int(userCommand), player)
        xo.showGameMap()
        return 1

if __name__ == '__main__':
    main()
