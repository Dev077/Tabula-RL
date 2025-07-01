from GridWorldEnv import GridWorldEnv
from QLearningAgent import QLearningAgent

env = GridWorldEnv()
agent = QLearningAgent(action=['up', 'down', 'left', 'right'])
episodes = 1000
steps = 0

for episode in range(episodes):
    state = env.reset()
    done = False
    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.learn(state, action, reward, next_state, done)
        state = next_state
        steps += 1
    
    if episode % 100 == 0:
        print(f"Episode {episode}, Steps: {steps}, Final State: {state}")
