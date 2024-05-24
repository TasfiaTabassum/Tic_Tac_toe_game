# src/mode/alpha_beta_pruning.py
import random

class AlphaBetaPruning:
    def __init__(self):
        pass

    def get_move(self, board, marker):
        possible_moves = board.get_possible_moves()
        random.shuffle(possible_moves)  # Shuffle the list of possible moves
        best_score = float('-inf')
        best_move = None
        alpha = float('-inf')
        beta = float('inf')

        for move in possible_moves:
            i, j = move
            board.board[i][j] = marker
            score = self.minimax(board, False, marker, alpha, beta)
            board.board[i][j] = ' '

            if score > best_score:
                best_score = score
                best_move = (i, j)

            alpha = max(alpha, best_score)
            if alpha >= beta:
                break

        if best_move is None:
            return self.get_random_move(board)

        return best_move


    def minimax(self, board, is_maximizing, marker, alpha, beta):
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
                        score = self.minimax(board, False, marker, alpha, beta)
                        board.board[i][j] = ' '
                        best_score = max(score, best_score)
                        alpha = max(alpha, best_score)
                        if alpha >= beta:
                            break
            return best_score
        else:
            best_score = float('inf')
            for i in range(board.size):
                for j in range(board.size):
                    if board.board[i][j] == ' ':
                        board.board[i][j] = 'X' if marker == 'O' else 'O'
                        score = self.minimax(board, True, marker, alpha, beta)
                        board.board[i][j] = ' '
                        best_score = min(score, best_score)
                        beta = min(beta, best_score)
                        if alpha >= beta:
                            break
            return best_score

    def get_random_move(self, board):
        possible_moves = board.get_possible_moves()
        if possible_moves:
            return random.choice(possible_moves)
        else:
            return None