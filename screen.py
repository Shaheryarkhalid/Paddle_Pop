import pygame


class Playable_Screen(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

    def draw(self, screen):
        rectangle = pygame.Rect(
            screen.get_width() / 8,
            screen.get_height() / 8,
            (screen.get_width() / 4) * 3,
            (screen.get_height() / 4) * 3,
        )
        pygame.draw.rect(screen, "blue", rectangle, 2, border_radius=20)
