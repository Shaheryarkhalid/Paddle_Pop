import random
import pygame
from Constants import BALL_RADIUS
from circleshape import CircleShape


class Ball(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = BALL_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, BALL_RADIUS)

    def update(self, screen):
        self.position += self.velocity * 1.5
        if self.overrunning(screen):
            self.bounce()

    def bounce(self):
        random_angle = random.uniform(85, 90)
        self.velocity = self.velocity.rotate(random_angle)

    def overrunning(self, screen):
        virtual_screen_width = (screen.get_width() / 4) * 3 - 2 - self.radius
        if (
            self.position.x > (screen.get_width() / 8) + virtual_screen_width
            or self.position.x < screen.get_width() / 8 + self.radius
            or self.position.y < screen.get_height() / 8 + self.radius
        ):
            return True
        return False

    def killed(self, screen):
        virtual_screen_height = (screen.get_height() / 4) * 3 - 2 - self.radius
        if self.position.y > (screen.get_height() / 8) + virtual_screen_height:
            return True
        return False
