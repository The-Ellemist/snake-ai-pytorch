import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

"""

"""


class BangGame:

    def __init__(self):
        self.player_1_shields = 5
        self.player_2_shields = 5
        self.player_1_reload = 0
        self.player_2_reload = 0
        self.score = 0

    def reset(self):
        self.player_1_shields = 5
        self.player_2_shields = 5
        self.player_1_reload = 0
        self.player_2_reload = 0
        self.score = 0

    def play_step(self, player_1_action, player_2_action):
        reward = 0
        gameover = False
        self.score += 1
        if player_1_action[1] == 1:
            self.player_1_reload = 1
            self.player_1_shields = 5
            if player_2_action[0] == 1:
                self.player_2_shields -= 1
            elif player_2_action[1] == 1:
                self.player_2_reload = 1
                self.player_2_shields = 5
            elif player_2_action[2] == 1:
                if self.player_2_reload == 1:
                    reward -= 10
                    gameover = True
        elif player_1_action[0] == 1:
            self.player_1_shields -= 1
            if player_2_action[0] == 1:
                self.player_2_shields -= 1
            elif player_2_action[1] == 1:
                self.player_2_reload = 1
                self.player_2_shields = 5
            elif player_2_action[2] == 1:
                self.player_2_reload = 0
                self.player_2_shields = 5
                #reward += 1
        elif player_1_action[2] == 1:
            if player_2_action[0] == 1:
                self.player_2_shields -= 1
            elif player_2_action[1] == 1:
                reward += 20
                gameover = True
            elif player_2_action[2] == 1:
                self.player_2_shields = 5
                self.player_2_reload = 0
            self.player_1_shields = 5
            self.player_1_reload = 0
        if gameover:
            self.score = -self.score
        return reward, gameover, self.score