import pygame as pg
import time
import random as rand

pg.init()
pg.font.init()

clock = pg.time.Clock()



screenW,screenH = pg.display.Info().current_w-100, pg.display.Info().current_h-100
screen = pg.display.set_mode((screenW,screenH))

pg.display.set_caption("Ascend The Stars!")


def updateScreen():
    pass



mainloop = True

while mainloop:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            mainloop = False
            exit()


    updateScreen()
