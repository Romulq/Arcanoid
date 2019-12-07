f = open('high score.txt', 'r')


class GameStats:
    def __init__(self, settings):
        self.heart_left = settings.heart
        self.setting = settings
        self.game_active = False
        self.score = 0
        self.high_score = int(f.readline())

    def reset_stats(self):
        self.heart_left = self.setting.heart
        self.score = 0
