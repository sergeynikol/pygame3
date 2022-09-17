import pygame
import controls, appSettins
from flash import Fire
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from flash import Fire



    
def run_game():
        pygame.init()
        pygame.mixer.music.load(appSettins.MUSIC["track1"])
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)

        screen = appSettins.screen 
        pygame.display.set_caption("Lukas Kill")
        bg_color =  appSettins.bg_color
        gun = Gun(screen)
        flash_1 = Fire(screen, gun)
        bullets = Group()
        inos = Group()
        controls.create_army(screen, inos)
        stats = Stats()
        sc = Scores(screen, stats)

        while True:
            controls.events(screen, gun, bullets)
            if stats.run_game:
                gun.update_gun()
                flash_1.update_flash(gun)
                controls.update(bg_color, screen, stats, sc, gun, flash_1, inos, bullets)
                controls.update_bullets(screen, stats, sc, inos, bullets)
                controls.update_inos(stats, screen, sc, gun, inos, bullets)
run_game()