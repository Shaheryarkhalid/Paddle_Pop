import pygame


class CircleShape(pygame.sprite.Sprite):

    def __init__(self, x, y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.radius = 20
        self.velocity = pygame.Vector2(3, 3)

    def draw(self, screen):
        pass

    def update(self, screen):
        pass

    def colliding(self, circleshape):
        distance = self.position.distance_to(circleshape.position)
        if distance <= self.radius + circleshape.radius:
            return True
        return False

    def bounce(self):
        # random_angle = random.uniform(20, 50)
        self.velocity = self.velocity.rotate(45)
