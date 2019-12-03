import pygame.ftfont
from pygame.sprite import Group
from heart import Heart


class Scoreboard:
    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.text_color = (163, 39, 39)
        self.font = pygame.font.SysFont('Rockwell', 36)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_heart()

    def prep_score(self):
        score_str = str(self.stats.score)
        rouded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rouded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10

    def prep_heart(self):
        self.hearts = Group()
        for heart_number in range(self.stats.heart_left):
            heart = Heart(self.settings.heart, self.screen)
            heart.rect.x = 5 + heart_number * heart.rect.width
            heart.rect.y = self.screen_rect.bottom - 36
            self.hearts.add(heart)

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, None)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.hearts.draw(self.screen)
