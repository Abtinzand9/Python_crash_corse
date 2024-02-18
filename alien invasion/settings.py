class Settings:
    """a class to store setting for the game"""
    def __init__(self):
        """initialize the game's settings"""
        #screem settings
        self.defult_screen_width = 1200
        self.defult_screen_heght = 800
        self.screen_width= 1200
        self.screen_heght = 800
        self.bg_color = (230,230,230)

        #ship setting
        self.ship_speed = 4
        self.ship_limit =3

        #bullet settings
        self.bullet_speed = 4
        self.bullet_width =3
        self.bullet_height =11
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 5

        #alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # fleet_directon means right when it is 1 and left when it is -1
        self.fleet_direction = 1