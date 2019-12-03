import pygame


class Ball:
    def __init__(self, settings, screen, paddle, bricks):
        self.screen = screen
        self.paddle = paddle
        self.bricks = bricks
        self.settings = settings

        self.positionx = float(self.paddle.rect.centerx)
        self.positiony = self.paddle.rect.top - 16
        self.position = (int(self.positionx), self.positiony)
        self.color = 0, 0, 0

        self.screen_rect = screen.get_rect()
        self.img = pygame.image.load('img/ballBlue.png')
        self.rect = pygame.draw.circle(screen, self.color, self.position, 10)

        self.speed_factor = 0
        self.speed_factorx = settings.ball_speed_factorx
        self.speed_factory = settings.ball_speed_factory
        self.ball_in_game = False

        self.y = float(self.rect.y)  # позиция шара y во время полета
        self.x = float(self.rect.x)

    def update(self):
        if self.ball_in_game:
            if (self.rect.centerx + self.speed_factorx > self.screen_rect.width - 10) or (
                    self.rect.centerx + self.speed_factorx < 10):
                self.speed_factorx = -self.speed_factorx
            elif self.rect.centery + self.speed_factory < 10:
                self.speed_factory = -self.speed_factory

            self.positionx += self.speed_factorx
            self.rect.x = self.positionx
            self.positiony = float(self.positiony) + self.speed_factory
            self.rect.y = self.positiony

        else:
            self.rect.x = self.paddle.rect.centerx - 10
            self.positionx = float(self.rect.x)  # позиция шара x до запуска

    def blitme(self):
        self.screen.blit(self.img, self.rect)
