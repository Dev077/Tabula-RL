# Q-Learning GridWorld Agent

> *"Instead of trying to produce a program to simulate the adult mind, why not rather try to produce one which simulates the child?"* — Alan Turing

A reinforcement learning project that implements a Q-learning agent navigating a 5×5 GridWorld — inspired by Alan Turing’s idea of the *child machine*. The agent learns from scratch to reach a goal through trial, error, and improvement over time.

---

## Features

- Q-Learning from scratch  
- ε-Greedy exploration with decay  
- Console-based grid visualization  
- Custom GridWorld environment  
- Save/load Q-table using `pickle`  
- Planned: random obstacles, multiple agents, hyperparameter sweeps

---

## Background

### Q-Learning

A model-free, value-based RL algorithm that learns optimal action policies by updating a table of state-action values:

```

Q(s, a) ← Q(s, a) + α · \[r + γ · maxₐ′ Q(s′, a′) − Q(s, a)]

````

- **α (alpha):** learning rate  
- **γ (gamma):** discount factor  
- **ε (epsilon):** exploration rate

### ε-Greedy Policy

Balances exploration and exploitation:
- With probability **ε**, choose a random action (explore)
- With probability **1−ε**, choose the best known action (exploit)

---

## Results

| Episode | Steps to Goal |
|---------|----------------|
| 0       | 108            |
| 100     | 4              |
| 500     | 5              |
| 900     | 2              |

> The agent quickly learns to reduce the number of steps to reach the goal, converging on optimal behavior within a few hundred episodes.

---

## Visual Demo

```text
 .  .  .  .  .
 .  A  .  .  .
 .  .  .  .  .
 .  .  .  .  .
 .  .  .  .  G
````

* `A` = Agent
* `G` = Goal
* `.` = Empty cell

Agent movement is animated during test runs using terminal updates.

---

## How to Run

```bash
git clone https://github.com/<your-username>/Tabula-RL.git
cd Tabula-RL
python TrainingLoop.py
```

Requirements:

* Python 3.8+
* No external libraries (optional: `matplotlib` for plots)

---

## Planned Experiments

| Parameter       | Description            | Default | Variants Tried      |
| --------------- | ---------------------- | ------- | ------------------- |
| `alpha`         | Learning rate          | 0.1     | 0.01, 0.5, 0.9      |
| `gamma`         | Discount factor        | 0.9     | 0.5, 0.95, 0.99     |
| `epsilon`       | Exploration rate       | 0.1     | 0.2, 0.5, 0.01      |
| `epsilon_decay` | Exploration decay rate | 0.995   | 0.99, 0.999, linear |

Results & insights from these runs will be documented below.

---

## Inspiration

This project draws direct inspiration from:

* Alan Turing’s idea of the “child machine”
* Sutton & Barto’s *Reinforcement Learning: An Introduction*
* OpenAI Gym and other gridworld-based teaching tools

---

## Acknowledgements

* Alan Turing (1950), [*Computing Machinery and Intelligence*](https://www.cs.mcgill.ca/~dprecup/courses/AI/Materials/turing1950.pdf)

```
