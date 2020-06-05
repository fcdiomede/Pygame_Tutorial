#Snake Tutorial Python

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass
        
    def move(self, dirnx, dirny):
        pass
    
    def draw(self, surface, eyes=False):
        pass
        

class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        #keeps track of which direction we are moving in
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                #elifs prevent clicking more than one key at once
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        #get index and cube in body list
        for i, c in enumerate(self.body):
            #all of cube objects have a position
            #grab that position
            p = c.pos[:]
            #is that position in our turn list?
            if p in self.turns:
                #if so, grab the turn direction
                turn = self.turns[p]
                #use method move to move in the right x,y direction
                c.move(turn[0], turn[1])
                #if we hit the last cube in the snake body, remove the turn
                #otherwise we would auto turn if we went over the same stop
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                #if we are moving left and we have reached the edge of the screen
                #change so that we go to the right side of the screen
                #do this for each direction
                if c.dirnx == -1 and c.pos[0] <= 0: 
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: 
                    c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: 
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: 
                    c.pos = (c.pos[0],c.rows-1)
                # If we haven't reached the edge just move in our current direction
                else: 
                    c.move(c.dirnx,c.dirny)  
        

    def reset(self, pos):
        pass

    def addCube(self):
        pass
        

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                #when we draw the first snake object, add eye to it
                c.draw(surface, True)
            else:
                c.draw(surface)


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y=0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        #draw two lines with every loop
        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))
        

def redrawWindow(surface):
    global rows, width, s
    surface.fill((0,0,0))
    s.draw(surface)
    drawGrid(width, rows, surface)
    pygame. display.update()


def randomSnack(rows, item):
    pass


def message_box(subject, content):
    pass


def main():
    global width, rows, s
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255,0,0), (10,10))

    clock = pygame.time.Clock()

    flag = True
    while flag:
        pygame.time.delay(50)
        #makes sure the game doesn't run more than 10 blocks per second
        clock.tick(10)

        redrawWindow(win)



main()