import pygame as pg
import time
import random as rand
import sys
rand.seed(420)


pg.init()
pg.font.init()

clock = pg.time.Clock()

screenW,screenH = pg.display.Info().current_w-100, pg.display.Info().current_h-100
screen = pg.display.set_mode((screenW,screenH))

pg.display.set_caption("Ascend The Stars!")

characters = ["Bottom.jpg", "star.png"]

class Character(object):
    def __init__(self,name,image,width,height,pos):
        self.name = name
        self.image = pg.image.load(image)
        self.width = width
        self.height = height
        self.x,self.y = pos

    def draw(self):
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        screen.blit(self.image, (self.x, self.y))

    def Rect(self):
        return pg.Rect(self.x,self.y,self.width,self.height)

class CurrentCharacter(Character):
    def __init__(self,name,image,width,height,pos,speed):
        self.name = name
        self.image = pg.image.load(image)
        self.images = [self.image]
        self.width = width
        self.height = height
        self.x,self.y = pos
        self.speed = speed
        self.rect = self.image.get_rect()
        self.th = self.height
        self.tw = self.width

    def Rect(self):
        self.rect = pg.Rect(self.x,self.y,self.tw,self.th)
        return self.rect

    def run(self):
        self.rect = self.Rect()
        if keys[pg.K_LEFT] and self.x > 0+self.width:
            self.x -= self.speed
            for i in self.images[1:]:
                i.x -= self.speed


        if keys[pg.K_RIGHT] and self.x < screenW - self.width:
            self.x += self.speed
            for i in self.images[1:]:
                i.x += self.speed

        if keys[pg.K_UP] and self.y > 0+self.height:
            self.y -= self.speed
            for i in self.images[1:]:
                i.y -= self.speed

        if keys[pg.K_DOWN] and self.y < screenH - self.height:
            self.y += self.speed
            for i in self.images[1:]:
                i.y += self.speed


        for x in collidables:
            if self.rect.colliderect(x.Rect()):
                self.images.append(x)

                self.x = min(self.x,x.x)
                self.y = min(self.y,x.y)

                self.tw = max(self.x+self.width,x.x+x.width)-self.x
                self.th = max(self.y+self.height,x.y+x.height)-self.y

                collidables.remove(x)

    def transform(self):
        global stage
        if len(self.images) > 30:
            self.images.clear()
            stage += 1
            self.image = pg.image.load(characters[stage])


    def draw(self,screen):
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        screen.blit(self.image, (self.x, self.y))

        for i in self.images[1:]:
            i.image = pg.transform.scale(i.image, (i.width, i.height))
            screen.blit(i.image, (i.x, i.y))


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

def generate(name,image, integer, rangex,rangey, width,height):
    global collidables

    for x in range(integer):
        collidables.append(Character(name,image,width,height,(rand.randint(rangex[0]+width,rangex[1]-width),rand.randint(rangey[0]+height,rangey[1]-height))))



def drawBackground(image):
    image = pg.image.load(image)
    image = pg.transform.scale(image, (screenW, screenH))
    screen.blit(image, (0, 0))


def updateScreen():
    drawBackground(currentBackground)
    for x in collidables:
        x.draw()

    player.run()
    player.draw(screen)
    player.transform()

    pg.display.update()

stage = 0
mainloop = True
player = CurrentCharacter("name", characters[stage],25,25,(screenW//2,screenH//2),2)
currentBackground = "C:\\Users\\Oat_M\\Dropbox\\PC\\Documents\\GitHub\\Ascend\\assets\\Section1.png"
collidables = []
generate("name","C:\\Users\\Oat_M\\Dropbox\\PC\\Documents\\GitHub\\Ascend\\assets\\Bottom.jpg",30,(0,screenW),(0,screenH),20,20)

while mainloop:
    clock.tick(500)
    keys = pg.key.get_pressed()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            mainloop = False
            exit()


    updateScreen()
