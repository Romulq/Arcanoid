import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from paddle import Paddle
from ball import Ball
import game_function as gf


def rungame():
    pygame.init()
    clock = pygame.time.Clock()

    gg = Settings()
    screen = pygame.display.set_mode(gg.size)
    stats = GameStats(gg)
    sb = Scoreboard(gg, screen, stats)

    pygame.display.set_caption("Arcanoid")

    play_button = Button(screen, u'Играть', 320, 445)
    rules_button = Button(screen, u'Правила', 320, 520)

    paddle = Paddle(gg, screen)
    bricks = Group()
    ball = Ball(gg, screen, paddle, bricks)

    gf.create_bricks(gg, screen, paddle, bricks)

    while True:
        gf.check_events(gg, screen, stats, play_button, rules_button, paddle, sb, bricks, ball)

        if stats.game_active:
            paddle.update()

            gf.update_ball(gg, screen, stats, paddle, sb, bricks, ball)

            gf.update_bricks(bricks)

        gf.update_screen(gg, screen, stats, sb, paddle, bricks, ball, play_button, rules_button)

        clock.tick(60)


rungame()
