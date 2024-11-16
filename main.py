import pygame as pg
import time
import random as rand

pg.init()
pg.font.init()

clock = pg.time.Clock()



screenW,screenH = pg.display.Info().current_w-100, pg.display.Info().current_h-100
screen = pg.display.set_mode((screenW,screenH))

pg.display.set_caption("Ascend The Stars!")

class Character(object):
    def __init__(self,name,image,width,height):
        self.name = name
        self.image = image
        self.width = width
        self.height = height

    def draw():
        pass

class CurrentCharacter(Character):
    def __init__(self,name,image,width,height,pos):
        self.name = name
        self.image = image
        self.width = width
        self.height = height
        self.x,self.y = pos

        

class Button(object):
    def __init__(self,image,width, height, pos,function):
        self.image = image
        self.width = width
        self.height = height
        self.x,self.y = pos
        self.function = function

        self.rect = pg.draw.rect(screen,(0,0,0),(self.x,self.y,self.width,self.height))

    def on_click(self):
        x, y = pg.mouse.get_pos()
        
        if self.rect.collidepoint(x, y):
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    self.function()



def updateScreen():
    pass


mainloop = True

while mainloop:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            mainloop = False
            exit()


    updateScreen()
