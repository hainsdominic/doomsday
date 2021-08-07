#!/usr/bin/python3

import pygame
from pygame.locals import KEYDOWN, QUIT, K_ESCAPE, K_a, K_d
import os
import random

from data.player import Player
from data.meteor import Meteor

SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

pygame.init()

GAME_OVER_FONT = pygame.font.SysFont("freemono", 80)
SCORE_FONT = pygame.font.SysFont("freemono", 25)

clock = pygame.time.Clock()

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Doomsday")

background = pygame.image.load(
    os.path.join("ressources", "images", "background.png")
).convert()

player_image = pygame.image.load(
    os.path.join("ressources", "images", "player.png")
).convert_alpha()

meteor_image = pygame.image.load(
    os.path.join("ressources", "images", "meteor.png")
).convert_alpha()

HIT = pygame.USEREVENT + 1


def handle_player_movement(pressed_keys, player):
    if pressed_keys[K_a] and player.pos.left - player.speed > 0:  # left
        player.move(-1)
    if pressed_keys[K_d] and player.pos.right + player.speed < SCREEN_WIDTH:  # right
        player.move(1)


def handleCollision(player, meteors):
    for meteor in meteors:
        if player.pos.colliderect(meteor.pos):
            pygame.event.post(pygame.event.Event(HIT))
            meteors.remove(meteor)


def draw_game_over():
    draw_text = GAME_OVER_FONT.render("GAME OVER", 1, (0, 0, 0))
    win.blit(
        draw_text,
        (
            SCREEN_WIDTH / 2 - draw_text.get_width() / 2,
            SCREEN_HEIGHT / 2 - draw_text.get_height() / 2,
        ),
    )
    pygame.display.flip()
    pygame.time.delay(3000)
    win.blit(background, (0, 0))


def get_high_score():
    # If the files doesnt exists, will return 0 as the high score
    try:
        f = open("score.txt", "r")
        return int(f.read())
    except:
        return 0


def write_high_score(score):
    f = open("score.txt", "w")
    f.write(str(score))
    f.close()


def main():
    running = True
    win.blit(background, (0, 0))

    player = Player(
        player_image,
        SCREEN_WIDTH / 2 - player_image.get_width() / 2,
        SCREEN_HEIGHT - player_image.get_height(),
        5,
    )

    ticks = 0
    meteors = []

    score = 0
    highscore = get_high_score()

    while running:
        win.blit(background, (0, 0))
        score = ticks // 5
        score_text = SCORE_FONT.render("Score: " + str(score), 1, (255, 255, 255))
        win.blit(
            score_text,
            (0, 0),
        )
        high_score_text = SCORE_FONT.render(
            "Highest: " + str(highscore), 1, (255, 255, 255)
        )
        win.blit(
            high_score_text,
            (0, 30),
        )

        clock.tick(60)
        ticks += 1
        if ticks % 50 == 0:  # Creates new meteor every 50 ticks
            new_meteor = Meteor(
                meteor_image,
                random.randrange(0, SCREEN_WIDTH - meteor_image.get_width() / 2),
                0,
                random.randrange(2, 7),
            )
            meteors.append(new_meteor)

        win.blit(player.image, player.pos)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            if event.type == HIT:
                if score > highscore:
                    highscore = score
                    write_high_score(score)
                draw_game_over()
                meteors = []
                ticks = 0

        pressed_keys = pygame.key.get_pressed()
        handle_player_movement(pressed_keys, player)

        handleCollision(player, meteors)

        for meteor in meteors:
            if meteor.pos.top > SCREEN_HEIGHT:
                meteors.remove(meteor)
            else:
                meteor.move()
                win.blit(meteor.image, meteor.pos)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
