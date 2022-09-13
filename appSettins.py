import pygame
import configparser

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) 
bg_color = (0, 0, 0)


"""real shit code"""
config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings.ini")  # читаем конфиг

APP_CAPTION=config["Main"]["appCaption"]
SCORE=config["Main"]["scoreFile"]

TRACK_1=config["Music"]["track1"]
TRACK_2=config["Music"]["track2"]
TRACK_3=config["Music"]["track3"]

FLASH_IMG=config["Img"]["flash"]
GUN_IMG=config["Img"]["gun"]
LIVE_IMG=config["Img"]["live"]
PIXEL_IMG=config["Img"]["pixel"]

pygame.mixer.init()
IMG = {
    1 : pygame.image.load('images/flach1.png').convert(),
    2 : pygame.image.load('images/gun.png').convert(),
    3 : pygame.image.load('images/heard.png').convert(),
    4 : pygame.image.load('images/mob1.png').convert_alpha(),
      }

MUSIC = {
    "track1": pygame.mixer.music.load("soungs/53341-lukashenko-menja-rasstreljali-na-vostochnoi-granic.mp3"),
    "track2": pygame.mixer.Sound("soungs/vyistrel-pistoleta-magnum-357-36128.ogg"),
    "track3": pygame.mixer.Sound("soungs/lukashenko-zhestochajshe.mp3"),
        }     