import enum
import pygame
from pygame.font import Font


class Menu(pygame.sprite.Sprite):

    def __init__(self, screen):
        self.position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.menu_list = ["Play", "Quit"]
        self.__font__ = pygame.font.Font(None, 100)
        self.__color__ = "white"
        self.selected = 0
        self.__timer__ = 0.2

    def draw(self, screen):
        for i, item in enumerate(self.menu_list):
            if i == self.selected:
                self.__color__ = "red"
            else:
                self.__color__ = "white"
            rendered_text = self.__font__.render(item, True, self.__color__)
            screen.blit(
                rendered_text,
                (self.position.x - 100, self.position.y - 330 + int(i * 110)),
            )

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.__timer__ -= dt
        if keys[pygame.K_UP]:
            if self.__timer__ <= 0:
                self.__timer__ = 0.2
                if self.selected > 0:
                    self.selected -= 1
                else:
                    self.selected = len(self.menu_list) - 1
        if keys[pygame.K_DOWN]:
            if self.__timer__ <= 0:
                self.__timer__ = 0.2
                if self.selected < len(self.menu_list) - 1:
                    self.selected += 1
                else:
                    self.selected = 0
