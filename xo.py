class Game:

    def __init__(self) -> None:
        self.map = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0
        ]
        self.showMap = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0
        ]

    def checkGame(self) -> int:
        ''' Check game
        0 - Have nothing
        1 - Block, we don't have any more moves available
        2 - Win
        '''
        gameMap = self.map
        if 0 not in gameMap:
            return 1
        elif gameMap[0] == 1 and gameMap[1] == 1 and gameMap[2] == 1 or gameMap[0] == 2 and gameMap[1] == 2 and gameMap[2] == 2:
            return 2
        elif gameMap[3] == 1 and gameMap[4] == 1 and gameMap[5] == 1 or gameMap[3] == 2 and gameMap[4] == 2 and gameMap[5] == 2:
            return 2
        elif gameMap[6] == 1 and gameMap[7] == 1 and gameMap[8] == 1 or gameMap[6] == 2 and gameMap[7] == 2 and gameMap[8] == 2:
            return 2
        elif gameMap[0] == 1 and gameMap[3] == 1 and gameMap[6] == 1 or gameMap[0] == 2 and gameMap[3] == 2 and gameMap[6] == 2:
            return 2
        elif gameMap[1] == 1 and gameMap[4] == 1 and gameMap[7] == 1 or gameMap[1] == 2 and gameMap[4] == 2 and gameMap[7] == 2:
            return 2
        elif gameMap[2] == 1 and gameMap[5] == 1 and gameMap[8] == 1 or gameMap[2] == 2 and gameMap[5] == 2 and gameMap[8] == 2:
            return 2
        elif gameMap[0] == 1 and gameMap[4] == 1 and gameMap[8] == 1 or gameMap[0] == 2 and gameMap[4] == 2 and gameMap[8] == 2:
            return 2
        elif gameMap[2] == 1 and gameMap[4] == 1 and gameMap[6] == 1 or gameMap[2] == 2 and gameMap[4] == 2 and gameMap[6] == 2:
            return 2
        else:
            return 0

    def gameMapDecoder(self) -> list:
        gameMap = self.map
        showMap = self.showMap
        for cell in range(len(gameMap)):
             showMap[cell] = "o" if gameMap[cell] == 1 else "x" if gameMap[cell] == 2 else "*"
        return showMap

    def showGameMap(self) -> None:
        gameMap = self.gameMapDecoder()
        print("\n".join([
            "Game map:",
            "",
            f" {gameMap[0]} | {gameMap[1]} | {gameMap[2]} ",
            "---+---+---",
            f" {gameMap[3]} | {gameMap[4]} | {gameMap[5]} ",
            "---+---+---",
            f" {gameMap[6]} | {gameMap[7]} | {gameMap[8]}"
        ]))
    
    def changeGameMap(self, userCommand: int, stateUser) -> None:
        '''Change status of cell witch user takes if it was not taked'''
        gameMap = self.map
        cellIndex = userCommand - 1
        if gameMap[cellIndex] != 1 or gameMap[cellIndex] != 2:
            gameMap[cellIndex] = 1 if stateUser == 2 else 2 if stateUser == 1 else None
