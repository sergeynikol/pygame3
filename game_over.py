import pygame,main,sys
from appSettins import IMG

class GameOv():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = IMG[5]
        self.image_rect = self.image.get_rect()

    def new_screen(self, screen) :
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            screen.fill("white")

            OPTIONS_TEXT = main.get_font(45).render("This is the OPTIONS screen.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = main.Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=main.get_font(75), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        main.main_menu()

            pygame.display.update()
    # def record_holder(self, stats):
    #     self.reset_stats()
    #     self.run_game = True
    #     with open('highscore.txt', 'r') as f:
    #         self.high_score = int(f.readline())