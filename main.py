# main.py
from src.game import play_game
from src.benchmark import benchmark
from src.plot_comparison import plot_metrics, calculate_win_rate


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'benchmark':
        results = benchmark()
        results = calculate_win_rate(results)
        plot_metrics(results)
    else:
        from src.game import play_game
        play_game()

