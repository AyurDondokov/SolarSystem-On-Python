import pygame, math
from Colors import *
WIDTH = 1080
HEIGHT = 800
FPS = 60

K_DIST = 80
K_RADIUS = 1/1000

class Planet():
    def __init__(self, screen, name, distance, radius, colorName, speed):
        self.__name = name
        self.__screen = screen
        self.__color = get_color(colorName)
        self.__distance = distance * K_DIST
        self.__radius = radius * K_RADIUS
        self.__rect = [WIDTH / 2, HEIGHT / 2 - distance, self.__radius * 2, self.__radius * 2]
        self.__speed = speed
        self.__angleRadian = 0
        self.__p = pygame.draw.circle(self.__screen, self.__color, (self.__rect[0], self.__rect[1]), self.__radius)
    def output(self):
        self.__angleRadian += self.__speed
        self.__rect[0] = math.cos(self.__angleRadian) * self.__distance + WIDTH / 2
        self.__rect[1] = math.sin(self.__angleRadian) * self.__distance + HEIGHT / 2
        self.__p = pygame.draw.circle(self.__screen, self.__color, (self.__rect[0],self.__rect[1]), self.__radius)
    def press(self, mouse):
        return (self.__p.collidepoint(mouse))

    def get_angle(self):
        return int(self.__angleRadian * 180 / math.pi % 360)

    def get_info(self):
        return self.__name + " - Угол:" + str(self.get_angle()) + ": Диаметр:" + str(self.__radius*2) + ": дистанция до Солнца:" + str(self.__distance)

