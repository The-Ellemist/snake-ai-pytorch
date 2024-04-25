import torch
import random
import numpy as np
from collections import deque
from bang import BangGame
from model import Linear_QNet, QTrainer
from helper import plot

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001


class Agent:

    def __int__(self):
        self.n_games = 0
        self.epsilon = 0  # randomness
        self.gamma = 0.9  # discount rate
        self.memory = deque(maxlen=MAX_MEMORY)  # popleft()
        self.model = Linear_QNet(11, 256, 3)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)

    def get_state(self, game, player_id):
        opponent_id = player_id + 1
        if opponent_id == 3:
            opponent_id = 1
        # (player id is 1 or 2)
        # the input:
        # if you have a reload
        # if the opponent has a reload
        # if you have more shields then the opponent
        state = [
            eval(f"game.player_{player_id}_reload"),
            eval(f"game.player_{opponent_id}_reload"),
            eval(f"game.player_{player_id}_shields > game.player_{opponent_id}_shields")
        ]
        return np.array(state, dtype=int)

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done)) # popleft if MAX_MEMORY is reached

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE) # list of tuples
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)
        #for state, action, reward, nexrt_state, done in mini_sample:
        #    self.trainer.train_step(state, action, reward, next_state, done)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):
        # random moves: tradeoff exploration / exploitation
        self.epsilon = 80 - self.n_games
        final_move = [0,0,0]
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 2)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1

        return final_move

def train()
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = BangGame()
    while True:
        # get old state
        state_old = agent.get_state(game, 1)

        # get move
        final_move = agent.get_action(state_old)

        # opponent move
        opponent_move = [0, 0, 0]
        opponent_move[random.randint(0, 2)] = 1

        # perform move and get new state
        reward, done, score = game.play_step(final_move, opponent_move)
        state_new = agent.get_state(game, 1)