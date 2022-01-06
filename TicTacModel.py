class Model():
    __game_board = [["(0,0)", "(0,1)", "(0,2)"],
                    ["(1,0)", "(1,1)", "(1,2)"],
                    ["(2,0)", "(2,1)", "(2,2)"]]
    def makeMove(self, x_coord, y_coord, player):
        if (self.__game_board[x_coord][y_coord].startswith("(")):
            self.__game_board[x_coord][y_coord] = player
            return True
        return False

    def getBoard(self):
        return self.__game_board

    def resetBoard(self):
        self.__game_board = [["(0,0)", "(0,1)", "(0,2)"],
                             ["(1,0)", "(1,1)", "(1,2)"],
                             ["(2,0)", "(2,1)", "(2,2)"]]