import pygame
from pygame.sprite import Sprite


class Heart(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('img/32x32.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)