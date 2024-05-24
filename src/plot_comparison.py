# src/plot_comparison.py
import matplotlib.pyplot as plt

def plot_metrics(results):
    metrics = ['depth', 'nodes_expanded', 'time', 'win_rate']
    modes = results.keys()
    
    for metric in metrics:
        fig, ax = plt.subplots()
        for mode in modes:
            data = [result[metric] for result in results[mode]]
            ax.plot(data, label=mode)

        ax.set_title(f'Comparison of {metric.capitalize()}')
        ax.set_xlabel('Game')
        ax.set_ylabel(metric.capitalize())
        ax.legend()
        plt.show()

def calculate_win_rate(results):
    win_rates = { 'minimax': 0, 'alpha_beta_pruning': 0, 'mcts': 0 }
    total_games = len(results['minimax'])

    for mode in win_rates.keys():
        wins = sum(1 for result in results[mode] if result['winner'] == 'X')
        win_rates[mode] = wins / total_games
    
    for mode in win_rates.keys():
        for result in results[mode]:
            result['win_rate'] = win_rates[mode]
    
    return results

if __name__ == "__main__":
    from .benchmark import benchmark
    results = benchmark()
    results = calculate_win_rate(results)
    plot_metrics(results)
