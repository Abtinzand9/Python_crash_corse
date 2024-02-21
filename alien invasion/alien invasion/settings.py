class Settings:
    """a class to store setting for the game"""
    def __init__(self):
        """initialize the game's static settings"""
        #screem settings
        self.defult_screen_width = 1200
        self.defult_screen_heght = 800
        self.screen_width= 1200
        self.screen_heght = 800
        self.bg_color = (230,230,230)

        #ship setting

        self.ship_limit =3
        #bullet settings
        self.bullet_width =3
        self.bullet_height =11
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 100

        #alien settings
        self.fleet_drop_speed = 100

        # how quickly the game speed up
        self.speed_up_scale = 1.1
        # how quickly scores speed up
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throught the game"""
        self.ship_speed = 4
        self.bullet_speed = 4
        self.alien_speed = 1
        # fleet_directon means right when it is 1 and left when it is -1
        self.fleet_direction = 1

        # scoring settings 
        self.alien_point = 50

    def increse_speed(self):
        """increase speed settings and alien point value"""
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale
        
        self.alien_point += int(self.alien_point * self.score_scale)