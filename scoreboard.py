import pygame.ftfont
from pygame.sprite import Group
from heart import Heart


class Scoreboard:
    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.text_color = (122, 1, 116, 0)
        self.font = pygame.font.SysFont('Alien Encounters', 36)

        self.prep_score()
        self.prep_high_score()
        self.prep_heart()

    def prep_score(self):
        rouded_score = int(round(self.stats.score))
        score_str = format(rouded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = self.screen_rect.top + 3

    def prep_heart(self):
        self.hearts = Group()
        for heart_number in range(self.stats.heart_left):
            heart = Heart(self.settings.heart, self.screen)
            heart.rect.x = 5 + heart_number * heart.rect.width
            heart.rect.y = self.screen_rect.bottom - 36
            self.hearts.add(heart)

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score))
        high_score_str = format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, None)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 3

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.hearts.draw(self.screen)
