import pygame
import configparser

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) 
bg_color = (0, 0, 0)
background_volume = pygame.mixer.music.set_volume(0.5)

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