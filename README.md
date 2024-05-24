# Tic Tac Toe Game

This repository contains a Python implementation of the classic Tic Tac Toe game, along with different playing modes including Minimax, Alpha-Beta Pruning, and Monte Carlo Tree Search (MCTS).

## Files

- **main.py**: Entry point for the game. Run this file to play Tic Tac Toe.
- **game.py**: Contains the logic for playing the game, including player turns and win conditions.
- **player.py**: Defines the Player class.
- **board.py**: Implements the game board and related functionalities.
- **benchmark.py**: Provides functionality to benchmark different playing modes.
- **plot_comparison.py**: Helps visualize the performance metrics of different playing modes.
- **mode/minimax.py**: Implements the Minimax playing mode.
- **mode/alpha_beta_pruning.py**: Implements the Alpha-Beta Pruning playing mode.
- **mode/mcts.py**: Implements the Monte Carlo Tree Search (MCTS) playing mode.

## How to Play

1. Run `main.py`.
2. Select a playing mode:
   - Minimax (Enter 1)
   - Alpha-Beta Pruning (Enter 2)
   - Monte Carlo Tree Search (Enter 3)
3. Follow the on-screen instructions to play the game.

## Benchmarking

To benchmark different playing modes, run `main.py` with the argument `benchmark`:

```python
python main.py benchmark
```

This will execute multiple games for each mode and display performance metrics such as depth, nodes expanded, time, and win rate.

## Plotting Comparison

To visualize the performance comparison between different playing modes, run `plot_comparison.py`.
