import pygame, sys

class Button():
    def __init__(self, screen, cord, imageWay, func):
        self.__screen = screen
        self.__image = pygame.image.load(imageWay)
        self.__rect = self.__image.get_rect()
        self.__rect.x = cord[0]
        self.__rect.y = cord[1]
        self.__func = func
    def is_press(self, mouse):
        return self.__rect.collidepoint(mouse)
    def press(self, mouse):
        if self.__rect.collidepoint(mouse):
            self.__func()
    def out(self):
        self.__screen.blit(self.__image, self.__rect)

    @property
    def function(self):
        return self.__func
    @function.setter
    def function(self, func):
        self.__func = func

class ProgressBar():
    def __init__(self, screen, cord, size, color):
        self.screen = screen
        self.cord = cord
        self.size = size
        self.color = color
        self.rect = [cord[0], cord[1], self.size[0], self.size[1]]

    def out(self, value, maxValue):
        self.rect[2] = self.size[0] * (value/maxValue)
        pygame.draw.rect(self.screen, self.color, self.rect)

class Text():
    def __init__(self, screen, text,  cord, size, fontWay, color):
        self.__screen = screen
        self.__cord = cord
        self.__color = color
        self.__font = pygame.font.Font(None, size)
        self.__text = self.__font.render(text, False, color)
    def out(self):
        self.__screen.blit(self.__text, self.__cord)

    @property
    def text(self):
        return self.__text
    @text.setter
    def text(self, text):
        self.__text = self.__font.render(text, False, self.__color)
    def change_text(self, text):
        self.__text = self.__font.render(text, False, self.__color)


