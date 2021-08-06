import pygame
from pygame.locals import KEYDOWN, QUIT, K_ESCAPE, K_SPACE, K_q, K_e

SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

pygame.mixer.init()
pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Doomsday")


def main():
    score = 0
    running = True
    gameStarted = False

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            pressed_keys = pygame.key.get_pressed()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
