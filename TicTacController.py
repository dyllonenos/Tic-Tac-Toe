from TicTacModel import Model

class Controller():
    winner = "Tie"
    def __init__(self):
        self.model = Model()
    def isGameOver(self):
        curr_game_board = self.model.getBoard()
        # Top Row is same
        if (curr_game_board[0][0] == curr_game_board[0][1] == curr_game_board[0][2]):
            self.winner = curr_game_board[0][0]
            return True

        # Middle Row is same
        elif (curr_game_board[1][0] == curr_game_board[1][1] == curr_game_board[1][2]):
            self.winner = curr_game_board[1][0]
            return True

        # Bottom Row is same
        elif (curr_game_board[2][0] == curr_game_board[2][1] == curr_game_board[2][2]):
            self.winner = curr_game_board[2][0]
            return True

        # Left Column is same
        elif (curr_game_board[0][0] == curr_game_board[1][0] == curr_game_board[2][0]):
            self.winner = curr_game_board[0][0]
            return True

        # Middle Column is same
        elif (curr_game_board[0][1] == curr_game_board[1][1] == curr_game_board[2][1]):
            self.winner = curr_game_board[0][1]
            return True

        # Right Column is same
        elif (curr_game_board[0][2] == curr_game_board[1][2] == curr_game_board[2][2]):
            self.winner = curr_game_board[0][2]
            return True

        # Left diagonal is same
        elif (curr_game_board[0][0] == curr_game_board[1][1] == curr_game_board[2][2]):
            self.winner = curr_game_board[0][0]
            return True

        # Right diagonal is same
        elif (curr_game_board[0][2] == curr_game_board[1][1] == curr_game_board[2][0]):
            self.winner = curr_game_board[0][2]
            return True

        # It was a tie
        elif (not curr_game_board[0][0].startswith("(") and 
                not curr_game_board[0][1].startswith("(") and 
                not curr_game_board[0][2].startswith("(") and 
                not curr_game_board[1][0].startswith("(") and 
                not curr_game_board[1][1].startswith("(") and 
                not curr_game_board[1][2].startswith("(") and 
                not curr_game_board[2][0].startswith("(") and 
                not curr_game_board[2][1].startswith("(") and 
                not curr_game_board[2][2].startswith("(")):
                return True

        else:
            return False

    def makeMove(self, x_coord, y_coord, player):
        return self.model.makeMove(x_coord, y_coord, player)

    def getBoard(self):
        return self.model.getBoard()
    
    def resetBoard(self):
        self.model.resetBoard()

    def getWinner(self):
        if (self.isGameOver() is True):
            return self.winner