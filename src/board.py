# src/board.py
import copy

class Board:
    def __init__(self, size=3):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.size * 2 - 1))

    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def place_marker(self, row, col, marker):
        if self.board[row][col] == ' ':
            self.board[row][col] = marker
            return True
        else:
            return False

    def check_winner(self, marker):
        # Check rows
        for row in self.board:
            if all(cell == marker for cell in row):
                return True

        # Check columns
        for col in range(self.size):
            if all(self.board[row][col] == marker for row in range(self.size)):
                return True

        # Check diagonals
        if all(self.board[i][i] == marker for i in range(self.size)) or \
                all(self.board[i][self.size - 1 - i] == marker for i in range(self.size)):
            return True

        return False

    def is_game_over(self):
        return self.is_full() or self.check_winner('X') or self.check_winner('O')

    def get_possible_moves(self):
        moves = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves

    def simulate_move(self, move):
        row, col = move
        marker = 'X' if self.get_current_player() == 'O' else 'O'
        new_board = Board(self.size)
        new_board.board = [row[:] for row in self.board]  # Copy current board
        new_board.place_marker(row, col, marker)
        return new_board

    def get_last_move(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == ' ':
                    return i, j

    def get_current_player(self):
        count_x = sum(row.count('X') for row in self.board)
        count_o = sum(row.count('O') for row in self.board)
        if count_x <= count_o:
            return 'X'
        else:
            return 'O'
        
    def copy(self):
        new_board = Board(self.size)
        new_board.board = copy.deepcopy(self.board)
        return new_board
