import pygame
from constants import *
from circleshape import *
from player import Player

class Lives(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS / 2)
        self.lives_max = PLAYER_MAX_LIVES
        self.lives_left = PLAYER_STARTING_LIVES
        self.more_lives = pygame.Vector2(PLAYER_RADIUS * 1.5, 0)
        self.positions = [self.position, self.position + self.more_lives,
                        self.position + 2 * self.more_lives, self.position + 3 * self.more_lives,
                        self.position + 4 * self.more_lives]
        
    def draw(self, screen):
        for life in range(0, self.lives_max):
            if life < self.lives_left:
                pygame.draw.circle(screen, "green", self.positions[life], self.radius, 0)
            else:
                pygame.draw.circle(screen, "red", self.positions[life], self.radius, 0)

    def update(self, object):
        if object.lives_left > self.lives_max:
            object.lives_left = self.lives_max
        else:
            self.lives_left = object.lives_left