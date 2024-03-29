import pygame


class Paddle:
    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('img/paddleBlu.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def center_paddle(self):
        self.center = self.screen_rect.centerx

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.paddle_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.paddle_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)