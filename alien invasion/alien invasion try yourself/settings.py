class settings :
    def __init__(self):
        # screen variables
        self.defult_screen_width = 1200
        self.defult_screen_heght = 800
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (71, 112, 76)

        # ship variables 
        self.ship_speed = 2.5
        self.ship_limit = 2

        #bullet settings
        self.bullet_speed = 10
        self.bullet_height = 4
        self.bullet_width = 10
        self.bullet_color = (0 , 0 ,0)
        self.bullets_allowed = 7

        #alien settings
        self.fleet_speed = 3
        # 1 for down -1 for up
        self.fleet_direction = 1
        self.fleet_move_close = 100

