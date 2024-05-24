# src/mode/minimax.py
import random

class Minimax:
    def __init__(self):
        pass

    def get_move(self, board, marker):
        possible_moves = board.get_possible_moves()
        random.shuffle(possible_moves)  # Shuffle the list of possible moves
        best_score = float('-inf')
        best_move = None

        for move in possible_moves:
            i, j = move
            board.board[i][j] = marker
            score = self.minimax(board, False, marker)
            board.board[i][j] = ' '

            if score > best_score:
                best_score = score
                best_move = (i, j)

        if best_move is None:
            return self.get_random_move(board)

        return best_move

    def minimax(self, board, is_maximizing, marker):
        if board.check_winner('X'):
            return -1
        elif board.check_winner('O'):
            return 1
        elif board.is_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(board.size):
                for j in range(board.size):
                    if board.board[i][j] == ' ':
                        board.board[i][j] = marker
                        score = self.minimax(board, False, marker)
                        board.board[i][j] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(board.size):
                for j in range(board.size):
                    if board.board[i][j] == ' ':
                        board.board[i][j] = 'X' if marker == 'O' else 'O'
                        score = self.minimax(board, True, marker)
                        board.board[i][j] = ' '
                        best_score = min(score, best_score)
            return best_score
        
    def get_random_move(self, board):
        possible_moves = board.get_possible_moves()
        if possible_moves:
            return random.choice(possible_moves)
        else:
            return None
