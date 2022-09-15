import pygame, sys
from button import Button
import pygame, controls, appSettins
from flash import Fire
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from flash import Fire

pygame.init()
SCREEN = appSettins.screen
appSettins.MUSIC["track4"]
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
BG = appSettins.IMG[6]


def run():
    pygame.init()
    pygame.mixer.init()
    appSettins.MUSIC["track1"]
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

    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = appSettins.get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=appSettins.get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():


    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = appSettins.get_font(50).render("MENU", True, "#b23f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(1000, 100))
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(1000, 230), 
                            text_input="Гульня", font=appSettins.get_font(55), base_color="#d3fcd4", hovering_color="Red")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(1000, 600), 
                            text_input="Настройка", font=appSettins.get_font(25), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(1000, 750), 
                            text_input="ВЫХАД", font=appSettins.get_font(25), base_color="#d7fcd4", hovering_color="Red")
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.stop()
                    run()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()