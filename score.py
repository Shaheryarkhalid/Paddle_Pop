import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.__position__ = pygame.Vector2(
            screen.get_width() / 8 + (screen.get_width() / 4) * 3 - 350,
            screen.get_height() / 8 - 70,
        )
        self.__font__ = pygame.font.Font(None, 100)
        self.__color__ = "red"

    def draw(self, screen, score):
        rendered_text = self.__font__.render(f"Score: {score}", True, self.__color__)
        screen.blit(
            rendered_text,
            self.__position__,
        )
