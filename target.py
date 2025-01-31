import pygame
import random
from Constants import TARGET_RADIUS
from circleshape import CircleShape


class Target(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = TARGET_RADIUS[random.randrange(0, len(TARGET_RADIUS))]

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
