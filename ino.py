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
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вывод лука на экран"""
        self.screen.blit(self.image, self.rect)
        

    def update(self):
        """перемещение луко"""
        self.rect.y += random.randint(-1,1)
        self.rect.x += random.randint(-4,4)
        if self.rect.y or self.rect.x > self.screen:
            self.rect.y = self.rect.y 
            self.rect.x = self.rect.x

