import pygame, controls
from flash import Fire
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from flash import Fire

def run():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("soungs/53341-lukashenko-menja-rasstreljali-na-vostochnoi-granic.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) 
    pygame.display.set_caption("Lukas Kill")
    bg_color = (0, 0, 0)
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
            

run()
