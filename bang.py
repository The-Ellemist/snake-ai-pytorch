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
        self.number_of_games = 1

    def reset(self):
        self.player_1_shields = 5
        self.player_2_shields = 5
        self.player_1_reload = 0
        self.player_2_reload = 0
        self.score = 0

    def play_step(self, player_1_action, player_2_action):
        pri = self.number_of_games / 10 == int(self.number_of_games / 10)
        pri = True
        if pri:
            print(f"Player 1 shields: {self.player_1_shields}")
            print(f"Player 1 reload: {self.player_1_reload}")
            print(f"Player 2 shields: {self.player_2_shields}")
            print(f"Player 2 reload: {self.player_2_reload}")
            print()
        reward = 0
        gameover = False
        if player_1_action[1] == 1:
            if pri:
                print("Player 1 reloaded")
            self.player_1_reload = 1
            self.player_1_shields = 5
            if player_2_action[0] == 1:
                if pri:
                    print("Player 2 shielded")
                self.player_2_shields -= 1
            elif player_2_action[1] == 1:
                if pri:
                    print("Player 2 reloaded")
                self.player_2_reload = 1
                self.player_2_shields = 5
            elif player_2_action[2] == 1:
                if pri:
                    print("Player 2 shot")
                if self.player_2_reload == 1:
                    reward -= 10
                    gameover = True
        elif player_1_action[0] == 1:
            if pri:
                print("Player 1 shielded")
            self.player_1_shields -= 1
            if player_2_action[0] == 1:
                if pri:
                    print("Player 2 shielded")
                self.player_2_shields -= 1
            elif player_2_action[1] == 1:
                if pri:
                    print("Player 2 reloaded")
                self.player_2_reload = 1
                self.player_2_shields = 5
            elif player_2_action[2] == 1:
                if pri:
                    print("Player 2 shot")
                self.player_2_reload = 0
                self.player_2_shields = 5
                reward += 1
        elif player_1_action[2] == 1:
            if pri:
                if self.player_1_reload == 1:
                    print("Player 1 shot")
                else:
                    print("Player 1 tried to shoot")
            if player_2_action[0] == 1:
                if pri:
                    print("Player 2 shielded")
                self.player_2_shields -= 1
            elif player_2_action[1] == 1:
                if pri:
                    print("Player 2 reloaded")
                if self.player_1_reload == 1:
                    reward += 20
                    score = 1
                    gameover = True
                else:
                    self.player_2_reload = 1
                    self.player_2_shields = 5
            elif player_2_action[2] == 1:
                if pri:
                    if self.player_2_reload == 1:
                        print("Player 2 shot")
                    else:
                        print("Player 2 tried to shoot")
                if self.player_2_reload == 1:
                    self.player_2_shields = 5
                    self.player_2_reload = 0
                    if self.player_1_reload == 0:
                        reward -= 10
                        gameover = True
                else:
                    if self.player_1_reload == 1:
                        reward += 20
                        score = 1
                        gameover = True
            if self.player_1_reload == 1:
                self.player_1_shields = 5
                self.player_1_reload = 0
            else:
                reward -= 3
        if pri:
            print("-----------")
        if gameover:
            self.number_of_games += 1
        return reward, gameover, self.score