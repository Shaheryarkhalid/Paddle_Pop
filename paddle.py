import pygame
from circleshape import CircleShape
from Constants import PADDLE_HEIGHT, PADDLE_WIDTH


class Paddle(CircleShape):

    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width / 2, screen_height / 4 * 3)
        self.velocity = pygame.Vector2(20, 0)
        self.__rect__ = pygame.Rect(
            self.position.x, self.position.y, PADDLE_WIDTH, PADDLE_HEIGHT
        )
        self.__jiggle_velocity__ = pygame.Vector2(0, 3)
        self.__jiggle_frames__ = 0

    def draw(self, screen):
        self.__rect__ = pygame.Rect(
            self.position.x, self.position.y, PADDLE_WIDTH, PADDLE_HEIGHT
        )
        pygame.draw.rect(screen, "green", self.__rect__, 10)

    def update(self, screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if not self.__overrunning_left__(screen):
                self.position -= self.velocity
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if not self.__overrunning_right__(screen):
                self.position += self.velocity

        if self.__jiggle_frames__ >= 0:
            if self.__jiggle_frames__ >= 4:
                self.position += self.__jiggle_velocity__
                self.__jiggle_frames__ -= 1
            else:
                self.position -= self.__jiggle_velocity__
                self.__jiggle_frames__ -= 1

    def __overrunning_right__(self, screen):
        virtual_screen_width = (screen.get_width() / 4) * 3
        if (
            self.position.x
            > (screen.get_width() / 8) + virtual_screen_width - PADDLE_WIDTH - 4
        ):
            return True
        return False

    def __overrunning_left__(self, screen):
        if self.position.x <= screen.get_width() / 8 + 4:
            return True
        return False

    def colliding(self, circleshape):
        closest_x = max(
            self.__rect__.left, min(circleshape.position.x, self.__rect__.right)
        )
        closest_y = max(
            self.__rect__.top, min(circleshape.position.y, self.__rect__.bottom)
        )
        distance = circleshape.position.distance_to((closest_x, closest_y))
        return distance <= circleshape.radius

    def jiggle(self):
        self.__jiggle_frames__ = 6
