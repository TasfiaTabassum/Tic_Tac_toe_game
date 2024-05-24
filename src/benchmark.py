# src/benchmark.py
import time
import random
from .board import Board
from .mode.minimax import Minimax
from .mode.alpha_beta_pruning import AlphaBetaPruning
from .mode.mcts import MCTS

def play_game(mode):
    board = Board()
    turn = 0
    metrics = {
        'depth': 0,
        'nodes_expanded': 0,
        'time': 0,
    }

    while not board.is_full():
        current_player = 'X' if turn % 2 == 0 else 'O'
        
        start_time = time.time()
        move = mode.get_move(board, current_player)
        elapsed_time = time.time() - start_time

        if move is None:
            break

        row, col = move
        marker = 'X' if current_player == 'X' else 'O'
        board.place_marker(row, col, marker)

        # Update metrics
        metrics['time'] += elapsed_time
        metrics['depth'] += 1  # This is a simplified representation of depth
        metrics['nodes_expanded'] += 1  # Simplified count, update with actual nodes expanded if possible

        if board.check_winner(marker):
            metrics['winner'] = current_player
            return metrics
        
        turn += 1

    metrics['winner'] = 'draw'
    return metrics

def benchmark():
    modes = {
        'minimax': Minimax(),
        'alpha_beta_pruning': AlphaBetaPruning(),
        'mcts': MCTS()
    }
    
    results = { 'minimax': [], 'alpha_beta_pruning': [], 'mcts': [] }
    num_games = 10

    for name, mode in modes.items():
        for _ in range(num_games):
            result = play_game(mode)
            results[name].append(result)
    
    return results
