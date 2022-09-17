import pygame, sys
from button import Button
import appSettins
import options

def run():
    pygame.init()
    appSettins.MUSIC["track4"]
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    BG = appSettins.IMG[6]
    screen_WIDTH = round(pygame.display.get_desktop_sizes()[0][0])
    screen_HEIGHT = round(pygame.display.get_desktop_sizes()[0][1])
    BG = pygame.transform.scale(BG, (screen_WIDTH, screen_HEIGHT))


    while True:
        appSettins.screen.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = appSettins.get_font(50).render("MENU", True, "#b23f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(screen_WIDTH/2, screen_HEIGHT/6 - 90))
        PLAY_BUTTON = Button((appSettins.IMG[7]), pos=(screen_WIDTH/2, screen_HEIGHT/6), 
                                text_input="Гульня", font=appSettins.get_font(55), base_color="#d3fcd4", hovering_color="Red")
        OPTIONS_BUTTON = Button((appSettins.IMG[8]), pos=(screen_WIDTH - 300, screen_HEIGHT-180), 
                                text_input="Настройка", font=appSettins.get_font(25), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button((appSettins.IMG[8]), pos=(screen_WIDTH - 300, screen_HEIGHT-70), 
                                text_input="ВЫХАД", font=appSettins.get_font(25), base_color="#d7fcd4", hovering_color="Red")
        appSettins.screen.blit(MENU_TEXT, MENU_RECT)
        
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(appSettins.screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    import game
                    pygame.mixer.music.stop()
                    False 
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options.options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

run()