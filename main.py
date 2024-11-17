import pygame as pg
import time
import random as rand
import sys


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
    def __init__(self,name,image,width,height,pos,speed):
        self.name = name
        self.image = pg.image.load(image)
        self.width = width
        self.height = height
        self.x,self.y = pos
        self.speed = speed

    def run(self):
        if keys[pg.K_LEFT] and self.x > 0+self.width:self.x -= self.speed
            
        if keys[pg.K_RIGHT] and self.x < screenW - self.width:self.x += self.speed

        if keys[pg.K_UP] and self.y > 0+self.height:self.y -= self.speed

        if keys[pg.K_DOWN] and self.y < screenH - self.height:self.y += self.speed

        
    def draw(self,screen):
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        screen.blit(self.image, (self.x, self.y))

        

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


def drawBackground(image):
    image = pg.image.load(image)
    image = pg.transform.scale(image, (screenW, screenH))
    screen.blit(image, (0, 0))


def updateScreen():
    drawBackground(currentBackground)
    player.run()
    player.draw(screen)

    pg.display.update()


mainloop = True


player = CurrentCharacter("name","C:\\Users\\Oat_M\\Dropbox\\PC\\Documents\\GitHub\\Ascend\\assets\\Bottom.jpg",25,25,(0,0),2)
currentBackground = "C:\\Users\\Oat_M\\Dropbox\\PC\\Documents\\GitHub\\Ascend\\assets\\Section1.png"

while mainloop:
    clock.tick(500)
    keys = pg.key.get_pressed()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            mainloop = False
            exit()


    updateScreen()
