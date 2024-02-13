class Settings:
    """a class to store setting for the game"""
    def __init__(self):
        """initialize the game's settings"""
        #screem settings
        self.screen_width = 1200
        self.screen_heght = 800
        self.bg_color = (230,230,230)

        #ship setting
        self.ship_speed = 1.5

        #bullet settings
        self.bullet_speed = 2.0
        self.bullet_width =3
        self.bullet_height =11
        self.bullet_color = (60,60,60)