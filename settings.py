class Settings():
    """docstring for Settings"""
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 子弹相关属性设置
        self.bullet_speed_factor = 5.5
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 30

        # 外星人相关属性配置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 100
        # 设置外星人整体移动方向 1代表向右移， -1代表向左移
        self.fleet_direction = 1

        # 飞船相关信息设置
        self.ship_limit = 3
        self.ship_speed_factor = 2.5


