import random

class GridWorldEnv:
    def __init__(self):
        self.size = 5
        self.goal = (4, 4)
        self.agent_pos = None
        self.reset()

    def reset(self):
        while True:
            self.agent_pos = (random.randint(0, self.size - 1),
                              random.randint(0, self.size - 1))
            if self.agent_pos != self.goal:
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
        self.agent_pos = (new_row, new_col)

        reward = 10 if self.agent_pos == self.goal else -1
        done = self.agent_pos == self.goal
        return self.agent_pos, reward, done
