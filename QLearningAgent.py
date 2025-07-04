import random
from collections import defaultdict
import pickle

class QLearningAgent:
    def __init__(self, action, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = defaultdict(float)
        self.action = action
        self.alpha = alpha  
        self.gamma = gamma  
        self.epsilon = epsilon

    def choose_action(self, state, exploit_only = False):
        if exploit_only or random.random() > self.epsilon:
            # Choose the action with the highest Q-value for the current state
            q_values = {action: self.q_table[(state, action)] for action in self.action}
            max_q_value = max(q_values.values())
            best_actions = [action for action, value in q_values.items() if value == max_q_value]
            return random.choice(best_actions)
        else:
            # Choose a random action
            return random.choice(self.action)

    def learn(self, state, action, reward, next_state, done):
        if done: 
            target = reward
        else:
            next_q = max(self.q_table[(next_state, a)] for a in self.action)
            target = reward + self.gamma * next_q
        
        current_q = self.q_table[(state, action)]
        new_q = current_q + self.alpha * (target - current_q)
        self.q_table[(state, action)] = new_q
    
    def save_q_table(self, filename='q_table.pkl'):
        with open(filename, 'wb') as f:
            pickle.dump(dict(self.q_table), f)
        print(f"Q-table saved to {filename}")

    def load_q_table(self, filename='q_table.pkl'):
        try:
            with open(filename, 'rb') as f:
                self.q_table = defaultdict(float, pickle.load(f))
            print(f"Q-table loaded from {filename}")
        except FileNotFoundError:
            print(f"No Q-table file found at {filename}, starting fresh.")