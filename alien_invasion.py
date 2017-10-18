import sys
import pygame
from setting import Setting
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():

    pygame.init()
    ai_settings = Setting()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Kevin Pew Pew")
    play_button = Button (ai_settings,screen,"play")
    stats = GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)
    ship= Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    alien = Alien(ai_settings,screen)
    gf.create_fleet(ai_settings,screen,ship,aliens)

    while True:
        # screen.fill(ai_settings.bg_color)
        gf.check_events(ai_settings,screen,stats,sb, play_button,ship,aliens,bullets)


        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()
