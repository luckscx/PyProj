'''
Created on 07/02/2013

@author: Simon
'''
import pygame,os
from pygame.locals import *

class Objects:
    
    def __init__(self):
        pathWork = os.getcwd()
        pathHouse  = os.path.join(pathWork, os.path.join("images", "house"))
        self.top = pygame.image.load(os.path.join(pathHouse, "top.png"))
        self.pos = [0,0]
        self.houses = []
        self.addHouse(self.pos)
        self.houseGroup = pygame.sprite.RenderUpdates(self.houses)
        self.Clock = pygame.time.Clock()
        self.moveTimer = 0
        self.speed = [0,0]
        
    def controller(self, events, screenSize):
        tick = self.Clock.tick()
        self.moveTimer += tick
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_w:
                    self.speed[1] += 2
                if event.key == K_a:
                    self.speed[0] += 2
                if event.key == K_s:
                    self.speed[1] -= 2
                if event.key == K_d:
                    self.speed[0] -= 2
            if event.type == KEYUP:
                if event.key == K_w:
                    self.speed[1] -= 2
                if event.key == K_a:
                    self.speed[0] -= 2
                if event.key == K_s:
                    self.speed[1] += 2
                if event.key == K_d:
                    self.speed[0] += 2
        if self.moveTimer > 30:
            self.set_position()
            self.moveTimer = 0
        return self.houseGroup
    
    def set_position(self):
        for house in self.houses:
            if self.speed[0] != 0 or self.speed[1] != 0:
                print self.speed
                self.houses[self.houses.index(house)].rect = house.rect.move(self.speed)
            
    
    def addHouse(self, pos):
        sprite = pygame.sprite.Sprite()
        sprite.image = self.top
        sprite.rect = sprite.image.get_rect()
        sprite.rect = sprite.rect.move(self.pos)
        self.houses.append(sprite)