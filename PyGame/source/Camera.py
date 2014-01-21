'''
Created on 08/02/2013

@author: Simon
'''
import pygame,os
from pygame.locals import *
class View:
    
    def __init__(self):
        pathWork = os.getcwd()
        pathHouse  = os.path.join(pathWork, os.path.join("images","house"))
        
        self.background = pygame.image.load(os.path.join(pathHouse, "map.jpg"))
        size = list(self.background.get_size())
        self.background = pygame.transform.smoothscale(self.background, (int(size[0]*2),int(size[1]*2)))
        self.bgSprite = pygame.sprite.Sprite()
        self.bgSprite.image = self.background
        self.bgSprite.rect = self.bgSprite.image.get_rect()
        self.bgShow = pygame.Rect(2500,3000,800,600)
        self.bgCropped = pygame.Surface((800,600))   
        self.set_background() 
        
        self.speed = [0,0]
        self.Clock = pygame.time.Clock()
        self.moveTime = 0
        self.tick = 0
        self.cameradx = False
        self.cameradx = True
        
    def controller(self, events):
        self.tick = self.Clock.tick()
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_w:
                    self.speed[1] -= 2
                if event.key == K_a:
                    self.speed[0] -= 2
                if event.key == K_s:
                    self.speed[1] += 2
                if event.key == K_d:
                    self.speed[0] += 2
            if event.type == KEYUP:
                if event.key == K_w:
                    self.speed[1] += 2
                if event.key == K_a:
                    self.speed[0] += 2
                if event.key == K_s:
                    self.speed[1] -= 2
                if event.key == K_d:
                    self.speed[0] -= 2
        self.moveTime += self.tick
        if self.moveTime >= 30:
            bgSize = self.background.get_size()
            topleft = list(self.bgShow.topleft)
            width,height = self.bgShow.width, self.bgShow.height
            if (topleft[0] + self.speed[0] > 0 and
                topleft[0] + width + self.speed[0] < bgSize[0]):
                topleft[0] += self.speed[0]
                self.cameradx = True
            else:
                self.cameradx = False
            if (topleft[1] + self.speed[1] > 0 and
                topleft[1] + height + self.speed[1] < bgSize[1]):
                topleft[1] += self.speed[1]
                self.camerady = True
            else:
                self.camerady = False
            self.bgShow.topleft = topleft
            self.moveTime = 0
            if self.speed[0] != 0 or self.speed[1] != 0:
                self.set_background()
                return self.bgCropped.get_rect()
        return False
        
    def set_background(self):
        rect = self.bgShow.clip(self.background.get_rect())
        self.bgCropped.blit(self.background, (0,0), rect)
    