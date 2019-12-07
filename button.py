import pygame.ftfont


class Button:
    def __init__(self, screen, msg, x, y):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.x = x
        self.y = y

        self.text_color = (122, 1, 116, 0)
        self.font = pygame.font.SysFont('Comic Sans MS', 32)

        self.image = pygame.image.load('img/buttonDefault.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.centery = y

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = self.x
        self.msg_image_rect.centery = self.y - 5

    def draw_button(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
