import random
import pickle

class GridWorldEnv:
    def __init__(self):
        self.size = 7
        self.goal = (5, 6)
        self.agent_pos = None
        self.obstacles = set()
        self.generate_obstacles(self.size)
        self.reset()

    def reset(self):
        while True:
            self.agent_pos = (random.randint(0, self.size - 1),
                              random.randint(0, self.size - 1))
            if self.agent_pos != self.goal and self.agent_pos not in self.obstacles:
                break
        return self.agent_pos

    def step(self, action):
        delta = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        move = delta.get(action, (0, 0))
        new_row = min(max(self.agent_pos[0] + move[0], 0), self.size - 1)
        new_col = min(max(self.agent_pos[1] + move[1], 0), self.size - 1)
        new_pos = (new_row, new_col)
        if new_pos not in self.obstacles:
            self.agent_pos = new_pos

        reward = 10 if self.agent_pos == self.goal else -1
        done = self.agent_pos == self.goal
        return self.agent_pos, reward, done

    def generate_obstacles(self, num=5):
        self.obstacles.clear()
        while len(self.obstacles) < num:
            pos = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            if pos != self.goal:
                self.obstacles.add(pos)

    def save_map(self, filename='grid_map.pkl'):
        with open(filename, 'wb') as f:
            pickle.dump(self.obstacles, f)

    def load_map(self, filename='grid_map.pkl'):
        with open(filename, 'rb') as f:
            self.obstacles = pickle.load(f)


