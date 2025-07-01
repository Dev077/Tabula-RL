from GridWorldEnv import GridWorldEnv
from QLearningAgent import QLearningAgent
import time
import os

env = GridWorldEnv()
agent = QLearningAgent(action=['up', 'down', 'left', 'right'])
episodes = 5000
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


train_new = input("Train from scratch? (y/n): ").strip().lower() == 'y'
if not train_new:
    agent.load_q_table()
else:
    episodes = 1000
    for episode in range(episodes):
        env.generate_obstacles(num=5)
        state = env.reset()
        done = False
        steps = 0
        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.learn(state, action, reward, next_state, done)
            state = next_state
            steps += 1

        agent.epsilon = max(0.01, agent.epsilon * 0.995)

        if episode % 100 == 0:
            print(f"Episode {episode}, Steps: {steps}, Final State: {state}")

    agent.save_q_table() 
    env.save_map()


# if not train_new:
#     agent.load_q_table()
#     env.load_map()  # Load the obstacle layout used during training

print("\nTest run (no exploration):")
env.generate_obstacles(num=5)
state = env.reset()
done = False
steps = 0
while not done:
    action = agent.choose_action(state, exploit_only=True)
    state, reward, done = env.step(action)
    steps += 1
    print_grid(state, env.goal, obstacles=env.obstacles, size=env.size)
    print(f"Step {steps}: Action = {action}, State = {state}, Reward = {reward}")

