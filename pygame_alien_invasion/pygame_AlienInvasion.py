""" 
Game Description:
In Alien Invasion, the player controls a ship that appears at the bottom center of
the screen. The player can move the ship right and lef using the arrow keys and shoot 
bullets using the Spacebar. When the game begins, fleet of aliens fills the sky and moves
across and down the screen. The player shoots and destroys the aliens. If the player shoots all 
the aliens, a new fleet appears that moves faster than the previous fleet. If any alien hits the 
player's ship or reaches the bottom of the screen, the player loses a ship. If the player loses 
three ships, the game ends."""


from tokenize import group
import pygame
from pygame.sprite import Group
from alien import Alien
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # make the play button.
    play_button = Button(ai_settings, screen, 'Play')
    # create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # creat ship instance from imported class
    # make a ship, a group of aliens, a group of bullets.
    ship = Ship(ai_settings, screen)
    # creat alien instance from imported class
    # alien = Alien(ai_settings, screen)
    # make a group to store bullets in.
    bullets = Group()
    aliens = Group()

    # creat a fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb,
                        play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats,
                              sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats,
                             sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship,
                         aliens, bullets, play_button)


run_game()
