import pygame
from pygame.sprite import Sprite
from appSettins import IMG


class Gun(Sprite):

    
    def __init__(self, screen):
        """инициализация пушки"""
        super(Gun, self).__init__()
        self.screen = screen
        self.image = IMG[2]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

   


    def output(self):
        """рисование пушки"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """обновление позиции пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 10
        if self.mleft and self.rect.left > 0:
            self.center -= 10
        self.rect.centerx = self.center
        if self.rect.bottom != self.screen_rect.bottom : 
           self.rect.y -= 1

    def create_gun(self):
        """размещение пушки по центру внизу экрана"""
        self.center = self.screen_rect.centerx

class Ls(Sprite):

        def __init__(self, screen):
            """инициализация жизни"""
            super(Ls, self).__init__()
            self.screen = screen
            self.image = pygame.image.load('images/heard.png')
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
            
            
            
            
           