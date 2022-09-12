import pygame
import random

class Ino(pygame.sprite.Sprite):
    """класс одного лука"""

    def __init__(self, screen):
        """инициализируем и задаем начальную позицию"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixels.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speedy = 0
        self.speedx = 0

    def draw(self):
        """вывод лука на экран"""
        self.screen.blit(self.image, self.rect)
        

    def update(self):
        """перемещение луко"""
        self.rect.y += random.randint(-1,1)
        self.rect.x += random.randint(-4,4)
        
        if pygame.Rect.contains(self.screen_rect, self.rect):
            self.rect.y = self.rect.y 
            self.rect.x = self.rect.x
        else:
            self.rect.x = self.screen_rect.centerx
            self.rect.y += 2

