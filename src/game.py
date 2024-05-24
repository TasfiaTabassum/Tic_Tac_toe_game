# src/game.py
from .board import Board
from .mode.minimax import Minimax
from .mode.alpha_beta_pruning import AlphaBetaPruning
from .mode.mcts import MCTS
import random

def select_mode():
    print("Select a mode:")
    print("1. Minimax")
    print("2. Alpha-Beta Pruning")
    print("3. Monte Carlo Tree Search")

    mode_choice = input("Enter your choice (1/2/3): ")
    if mode_choice == "1":
        return Minimax()
    elif mode_choice == "2":
        return AlphaBetaPruning()
    elif mode_choice == "3":
        return MCTS()
    else:
        print("Invalid choice. Defaulting to Minimax.")
        return Minimax()

def play_game():
    mode = select_mode()
    board = Board()
    turn = 0

    board.display()  # Print initial board

    while not board.is_full():
        current_player = 'X' if turn % 2 == 0 else 'O'
        print(f"Player {current_player}'s turn")

        move = mode.get_move(board, current_player)
        if move:
            row, col = move
            if 0 <= row < board.size and 0 <= col < board.size:
                marker = 'X' if current_player == 'X' else 'O'
                if board.place_marker(row, col, marker):
                    board.display()  # Print board after each move
                    if board.check_winner(marker):
                        print(f"Player {current_player} wins!")
                        return
                    turn += 1
                else:
                    print("That position is already taken. Try again.")
            else:
                print("Invalid move. Row and column must be between 0 and 4.")
        else:
            print("No valid moves available. It's a draw!")
            return

    print("It's a draw!")
