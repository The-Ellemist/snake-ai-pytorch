import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

"""

"""


class BangGame():
    def __int__(self):
        self.reset()

    def reset(self):
        self.gameover = False
        self.player_1_shields = 5
        self.player_2_shields = 5
        self.player_1_reload = 0
        self.player_2_reload = 0

    def play_step(self, player_1_action, player_2_action):
        pass