# src/mode/mcts.py
import random
import math

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0

    def is_fully_expanded(self):
        return len(self.children) == len(self.state.get_possible_moves())

    def select_child(self, exploration_weight=1.41):
        best_score = -float('inf')
        best_child = None

        for child in self.children:
            exploitation = child.wins / child.visits
            exploration = math.sqrt(2 * math.log(self.visits) / child.visits)
            score = exploitation + exploration_weight * exploration
            if score > best_score:
                best_score = score
                best_child = child

        return best_child

class MCTS:
    def __init__(self, num_simulations=1000):
        self.num_simulations = num_simulations

    def get_move(self, board, marker):
        root = Node(board)
        for _ in range(self.num_simulations):
            node = self.select_node(root)
            winner = self.simulate(node)
            self.backpropagate(node, winner)

        best_child = root.select_child(exploration_weight=0)
        if best_child:
            return best_child.state.get_last_move()
        else:
            possible_moves = board.get_possible_moves()
            if possible_moves:
                return random.choice(possible_moves)
            else:
                return None



    def select_node(self, node):
        while not node.state.is_game_over():
            if not node.is_fully_expanded():
                return self.expand(node)
            else:
                node = node.select_child()
        return node

    def expand(self, node):
        possible_moves = node.state.get_possible_moves()
        untried_moves = [move for move in possible_moves if move not in [child.state.get_last_move() for child in node.children]]
        random_move = random.choice(untried_moves)
        new_state = node.state.simulate_move(random_move)
        new_node = Node(new_state, parent=node)
        node.children.append(new_node)
        return new_node

    def simulate(self, node):
        current_state = node.state.copy()
        while not current_state.is_game_over():
            possible_moves = current_state.get_possible_moves()
            random_move = random.choice(possible_moves)
            current_state = current_state.simulate_move(random_move)
        if current_state.check_winner('X'):
            return 'X'
        elif current_state.check_winner('O'):
            return 'O'
        else:
            return 'draw'

    def backpropagate(self, node, winner):
        while node is not None:
            node.visits += 1
            if winner == node.state.get_current_player():
                node.wins += 1
            node = node.parent
