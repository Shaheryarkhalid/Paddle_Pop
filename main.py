import pygame
from ball import Ball
import ball
from menu import Menu
from paddle import Paddle
from score import Score
from screen import Playable_Screen
from target import Target
from targetfield import TargetField


pygame.init()
SCREEN_HEIGHT = pygame.display.Info().current_h
SCREEN_WIDTH = pygame.display.Info().current_w


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
clock = pygame.time.Clock()
dt = 0
pygame.display.set_caption("Paddle Pop")

game_paused = True


def main():
    global dt
    global game_paused
    score = 0

    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    targets = pygame.sprite.Group()
    Playable_Screen.containers = drawables
    Paddle.containers = (drawables, updatables)
    Ball.containers = (drawables, updatables)
    Target.containers = (targets, drawables, updatables)
    TargetField.containers = updatables

    playable_screen = Playable_Screen()
    paddle = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT)
    bouncy_ball = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    targetfield = TargetField()
    score_display = Score(screen)

    menu = Menu(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        playable_screen.draw(screen)

        if game_paused:
            menu.draw(screen)
            menu.update(dt)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                if (
                    menu.menu_list[menu.selected] == "Play"
                    or menu.menu_list[menu.selected] == "Resume"
                ):
                    game_paused = False
                    menu.menu_list[0] = "Play"

                if (
                    menu.menu_list[menu.selected] == "Restart"
                    or menu.menu_list[menu.selected] == "Replay"
                ):
                    score = 0
                    paddle.kill()
                    paddle = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT)
                    bouncy_ball.kill()
                    bouncy_ball = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    for target in targets:
                        target.kill()
                    targetfield = TargetField()
                    game_paused = False

                if menu.menu_list[menu.selected] == "Quit":
                    return

            pygame.display.flip()
            dt = clock.tick(60) / 1000
            continue

        score_display.draw(screen, str(score))

        for obj in drawables:
            obj.draw(screen)

        for obj in updatables:
            obj.update(screen)

        for obj in targets:
            if bouncy_ball.colliding(obj):
                obj.kill()
                bouncy_ball.bounce()
                score += 1
                if len(targets) <= 5:
                    targetfield = TargetField()

        if paddle.colliding(bouncy_ball):
            bouncy_ball.bounce()
            paddle.jiggle()

        if bouncy_ball.killed(screen):
            bouncy_ball.kill()
            score = 0
            menu.menu_list[0] = "Replay"
            game_paused = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE]:
            game_paused = True
            menu.menu_list[0] = "Resume"
            if menu.menu_list[1] != "Restart":
                menu.menu_list.insert(1, "Restart")
        dt = clock.tick(60) / 1000
        pygame.display.flip()


if __name__ == "__main__":
    main()
