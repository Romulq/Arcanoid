import pygame


class Settings:
    def __init__(self):

        # ПАРАМЕТРЫ ПОЛЯ
        self.size = self.width, self.height = 640, 850
        self.bg_img = pygame.image.load('img/bg 640x856.jpg')

        # ПАРАМЕТРЫ
        self.heart = 3
        self.started = False
        self.paddle_speed_factor = 4.5
        self.ball_speed_factorx = 4.0
        self.ball_speed_factory = -4.0
        self.brick_points = 245

        # ТЕМП ИГРЫ
        self.speedup_scale = 1.1
        self.score_scale = 1.3




