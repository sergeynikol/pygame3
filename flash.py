import pygame


class Fire():
    """инициализация вспышки"""
    def __init__(self, screen, gun):
        self.screen = screen
        self.image = pygame.image.load('images/ fr_1.png').convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = gun.rect.centerx
        self.rect.bottom = gun.rect.top
        #self.up_flash = upd
      
             
    def flash(self):
        self.screen.blit(self.image, self.rect)

    def update_flash(self, gun):
        """обновление позиции вспышки"""
        self.rect.centerx = gun.rect.centerx
        self.rect.bottom = gun.rect.top