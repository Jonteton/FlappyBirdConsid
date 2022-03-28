from turtle import width


import pygame


class Pillar:
    def __init__(self, x, y, width, height, velocity_x,):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity_x = velocity_x

    def render(self, screen, pillar_gap_y, floor_y):
        pygame.draw.rect(screen, color="black", rect=(
            self.x, self.y, self.width, self.height))

        pygame.draw.rect(screen, color="black", rect=(
            self.x, self.height + pillar_gap_y, self.width, floor_y - self.height - pillar_gap_y + 45))

    def update_position(self):
        self.x = self.x - self.velocity_x
