class FBoard:
    def __init__(self, board_size=8):
        self.__game_state = "UNFINISHED"
        self.__game_board = [
            ["#" for i in range(board_size)] for i in range(board_size)]
        self.__x_piece = (5, 5)
        self.__o_pieces = [(1, 7),
                           (1, 6),
                           (1, 5),
                           (2, 7)
                           ]
        self.__game_board[self.__x_piece[0]][self.__x_piece[1]] = "X"
        for o in self.__o_pieces:
            self.__game_board[o[0]][o[1]] = "O"

    def get_game_state(self):
        return self.__game_state

    def move_x(self, x, y):

        if self.__game_state != "UNFINISHED":
            return False
        # Is piece only moving one spot
        if abs(self.__x_piece[0] - x) != 1 or abs(self.__x_piece[1] - y) != 1:
            return False

        legal_moves = self.get_legal_moves_x()

        if self.check_for_x_move(legal_moves):
            self.__game_state = "O_WON"
            return False

        if (x, y) not in legal_moves or legal_moves[(x, y)] == "False":
            return False

        self.mark_map(x, y, "X")

        if x == 7 and y == 7:
            self.__game_state = "X_WON"
        return True

    def get_legal_moves_x(self):
        current_x = self.__x_piece[0]
        current_y = self.__x_piece[1]
        legal_x_moves = {}
        legal_x_moves[(current_x-1, current_y-1)
                      ] = self.get_move_x(current_x-1, current_y-1)
        legal_x_moves[(current_x+1, current_y+1)
                      ] = self.get_move_x(current_x+1, current_y+1)
        legal_x_moves[(current_x-1, current_y+1)
                      ] = self.get_move_x(current_x-1, current_y+1)
        legal_x_moves[(current_x+1, current_y-1)
                      ] = self.get_move_x(current_x+1, current_y-1)
        return legal_x_moves

    def get_move_x(self, x, y):
        # if out side of the board
        if x < 0 or y < 0 or x > 7 or y > 7:
            return "False"
        # if square unoqupied
        return "True" if self.__game_board[x][y] == "#" else "False"

    def move_o(self, loc_x, loc_y, dest_x, dest_y):
        if self.__game_state != "UNFINISHED":
            return False

        if self.o_quick_check(loc_x, loc_y, dest_x, dest_y):
            self.mark_map(dest_x, dest_y, "O", loc_x, loc_y)
        else:
            return False
        # check to see if x has any moves left
        legal_moves = self.get_legal_moves_x()
        if self.check_for_x_move(legal_moves):
            self.__game_state = "O_WON"
            return True
        return True

    def o_quick_check(self, ox, oy, x, y):
        # are x,y off the board
        if x > 7 or x < 0 or y > 7 or y < 0:
            return False
        #x,y is occupied
        if self.__game_board[x][y] != "#":
            return False
        # check for "O" piece at given coord
        if self.__game_board[ox][oy] != "O":
            return False
        # x and y is bigger then origin
        if ox < x and oy < y:
            return False
        # if O is only moving one square
        if abs(ox - x) != 1 or abs(oy - y) != 1:
            return False
        return True
    # Helper Methods

    def mark_map(self, x, y, piece, present_x=0, present_y=0):
        if piece == "X":
            present_x = self.__x_piece[0]
            present_y = self.__x_piece[1]
            self.__x_piece = (x, y)
        self.__game_board[present_x][present_y] = "#"
        self.__game_board[x][y] = piece

    def check_for_x_move(self, legal_moves):
        # check to see if x has any moves left
        legal_moves = self.get_legal_moves_x()
        for move in legal_moves:
            if legal_moves[move] == 'True':
                return False
        else:
            return True

    def print_board(self):
        '''DEBUG: Prints current game board'''
        for square in self.__game_board:
            print(square)
