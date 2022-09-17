import pygame

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) 
bg_color = (0, 0, 0)
muz = pygame.mixer.music

pygame.mixer.init()

IMG = {

    1 : pygame.image.load('images/flach1.png').convert(),
    2 : pygame.image.load('images/gun.png').convert(),
    3 : pygame.image.load('images/heard.png').convert(),
    4 : pygame.image.load('images/mob1.png').convert_alpha(),
    5 : pygame.image.load('images/autozak.jpeg').convert_alpha(),
    6 : pygame.image.load('images/flagi-belarus-pagonya.jpg').convert(),
    7 : pygame.image.load('images/Play Rect.png'),
    8 : pygame.image.load('images/Quit Rect.png'),
    9 : pygame.image.load('images/flagi-belarus-pagonya.jpg'),

    }

MUSIC = {
    "track1": "soungs/menja-rasstreljali.mp3",
    "track2": pygame.mixer.Sound("soungs/magnum.ogg"),
    "track3": pygame.mixer.Sound("soungs/ghestochajshe.mp3"),
    "track4": "soungs/menu_musick.mp3"
        }

def get_font(size): 
    """настройка шрифтов меню"""
    return pygame.font.Font("assets/font.ttf", size)