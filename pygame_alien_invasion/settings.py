class Settings():
    """ A class to store all settings for Alien Invasion. """

    def __init__(self) -> None:
        """ initialize the game's static settings."""
        # screen settings
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (204, 230, 255)

        # ship settings
        self.ships_limit = 3

        # bullet settings
        self.bullet_speed_factor = 1.5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 102, 217)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # how quickly the game speed up.
        self.speedup_scale = 1.1
        # how quickly the alien point value increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ initialize settings that change throughout the game. """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction of 1 represents right: -1 represents left.
        self.fleet_direction = 1

        # scoring.
        self.alien_points = 50

    def increase_speed(self):
        """ increase alien speed settings and alien point values. """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
