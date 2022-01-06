from TicTacController import Controller

class GUIView():
    def __init__(self):
        self.controller = Controller()
    def start(self):
        print(self.controller.isGameOver())
        curr_game_board = self.controller.getBoard()
        self.print_board(curr_game_board)
        current_player_marker = "X"
        while (not self.controller.isGameOver()):
            user_input = str(input("Make your move "+ current_player_marker + " (x,y) : \n"))
            x_coord = int(user_input.split(",")[0])
            y_coord = int(user_input.split(",")[1])
            result = self.controller.makeMove(x_coord, y_coord, current_player_marker)
            new_board = self.controller.getBoard()
            self.print_board(new_board)
            # If it is a valid move we will swap players
            if (result == True):
                if (current_player_marker == "X"):
                    current_player_marker = "O"
                elif (current_player_marker == "O"):
                    current_player_marker = "X"
            # If it is not a valid move the current player will be the same to reattempt
            else:
                print("That spot is already taken choose a new one!")
        winner = self.controller.getWinner()
        print("Game Over")
        if (winner == "Tie"):
            print("It was a Tie")
        else:
            print(winner + " won the game!")

    def print_board(self, curr_game_board):
        for row in range(len(curr_game_board)):
            first_space = str(curr_game_board[row][0])
            second_space = str(curr_game_board[row][1])
            third_space = str(curr_game_board[row][2])
            if (first_space.startswith("(")):
                first_space = " "
            if (second_space.startswith("(")):
                second_space = " "
            if (third_space.startswith("(")):
                third_space = " "
            print(first_space + " | " + second_space + " | " + third_space)
            if (row != 2):
                print("----------")
if __name__ == "__main__":
    curr_game = GUIView()
    curr_game.start()