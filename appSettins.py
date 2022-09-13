import pygame

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) 
bg_color = (0, 0, 0)

pygame.mixer.init()
IMG = {
    "flash" : pygame.image.load('images/flach1.png').convert(),
    "gun"   : pygame.image.load('images/gun.png').convert(),
    "hearh" : pygame.image.load('images/heard.png').convert(),
    "mob"   : pygame.image.load('images/mob1.png').convert_alpha(),
      }

MUSIC = {
    "track1": pygame.mixer.music.load("soungs/53341-lukashenko-menja-rasstreljali-na-vostochnoi-granic.mp3"),
    "shot": pygame.mixer.Sound("soungs/vyistrel-pistoleta-magnum-357-36128.ogg"),
    "track3": pygame.mixer.Sound("soungs/lukashenko-zhestochajshe.mp3"),
        }     
