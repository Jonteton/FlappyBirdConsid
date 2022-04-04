from turtle import width
import time
import math

import pygame


class Pillar:
    def __init__(self, x, y, width, height, pillar_gap_y, ground_y, velocity_x):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Values used to create the second pillar below the first one
        self.x2 = self.x
        self.y2 = self.height + pillar_gap_y

        self.height2 = ground_y - self.y2

        self.velocity_x = velocity_x

    def render(self, screen):
        pygame.draw.rect(screen, color="black", rect=(
            self.x, self.y, self.width, self.height))

        pygame.draw.rect(screen, color="black", rect=(
            self.x, self.y2, self.width, self.height2))

    def update_position(self, startTime):
        now = time.time()
        self.x = self.x - self.velocity_x * (50 + now - startTime) / 750

    def freeze(self):
        self.velocity_x = 0
