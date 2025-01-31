import pygame
import random

from target import Target


class TargetField(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.__spawn_timer__ = 0.0
        self.__spawned_targets__ = 0

    def update(self, screen):
        self.__spawn_timer__ += 0.1
        if self.__spawn_timer__ >= 1 and self.__spawned_targets__ <= 20:
            self.__spawned_targets__ += 1
            self.__spawn__(screen)
            self.__spawn_timer__ = 0.0

    def __spawn__(self, screen):
        random_x = random.randrange(
            ((screen.get_width() // 8) + 20),
            ((screen.get_width() // 8) + (screen.get_width() // 4) * 3) - 20,
        )
        random_y = random.randrange(
            ((screen.get_height() // 8) + 20),
            ((screen.get_height() // 4) * 3) - 20,
        )
        target = Target(random_x, random_y)
