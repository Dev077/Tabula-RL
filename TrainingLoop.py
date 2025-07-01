from GridWorldEnv import GridWorldEnv
from QLearningAgent import QLearningAgent
import time
import os

env = GridWorldEnv()
agent = QLearningAgent(action=['up', 'down', 'left', 'right'])
episodes = 1000
steps = 0

def print_grid(agent_pos, goal_pos, obstacles=None, size=7):
    # os.system('cls' if os.name == 'nt' else 'clear')
    for r in range(size):
        row = ''
        for c in range(size):
            pos = (r, c)
            if pos == agent_pos:
                row += ' A '
            elif pos == goal_pos:
                row += ' G '
            elif obstacles and pos in obstacles:
                row += ' X '
            else:
                row += ' . '
        print(row)
    time.sleep(0.3)


for episode in range(episodes):
    state = env.reset()
    done = False
    steps = 0  # Reset steps count for each episode
    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.learn(state, action, reward, next_state, done)
        state = next_state
        steps += 1

    # Decay epsilon once per episode
    agent.epsilon = max(0.01, agent.epsilon * 0.995)

    if episode % 100 == 0:
        print(f"Episode {episode}, Steps: {steps}, Final State: {state}")


print("\nTest run (no exploration):")
state = env.reset()
done = False
steps = 0
while not done:
    action = agent.choose_action(state, exploit_only=True)
    state, reward, done = env.step(action)
    steps += 1
    print_grid(state, env.goal, obstacles=env.obstacles, size=env.size)
    print(f"Step {steps}: Action = {action}, State = {state}, Reward = {reward}")

