import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ A class to manage bullets from the ship. """

    def __init__(self, ai_settings, screen, ship) -> None:
        super().__init__()
        self.screen = screen

        # create bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """ move the bullet up. """
        # update the decimal position of the bullet.
        self.y -= self.speed_factor
        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """ draw tje bullet to screen. """

        pygame.draw.rect(self.screen, self.color, self.rect)
