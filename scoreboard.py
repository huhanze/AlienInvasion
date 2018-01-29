import pygame.font
from pygame.sprite import Group
from ship import Ship

# 记录得分信息
class Scoreboard():

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 设置显示得分信息使用的字体
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        # 初始化得分显示
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    # 渲染图像
    def prep_score(self):
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,self.ai_settings.bg_color)
        # 设置显示位置
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    # 最高得分
    def prep_high_score(self):
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,self.ai_settings.bg_color)

        # 将最高得分记录放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    # 等级
    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color,self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom


    # 在屏幕上显示得分
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)

    # 显示剩余的飞船数量
    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 20
            self.ships.add(ship)
