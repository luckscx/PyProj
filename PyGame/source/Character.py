'''
Created on 03/02/2013

@author: Simon
'''
import os, pygame
from pygame.locals import *

class Character:

    def __init__(self):
        pathWork = os.getcwd()
        pathChar  = os.path.join(pathWork, os.path.join("images", "character")) 
        self.charElements = {}
        self.load_elements(pathChar)
        self.speed = [0,0]
        self.position = [2500,3000]
        self.Clock = pygame.time.Clock()
        self.moveTime = 0
        self.animationCounter = 0 
        self.animationCounter2 = 0
        self.animationCounter3 = 10
        self.set_image()
        
        self.health = 100
        self.charGroup = pygame.sprite.RenderUpdates()
        print "Finished initiating Character module..."
            
    def controller(self, events, screen_size, sprite):
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
        self.moveTime += self.Clock.tick()
        if self.moveTime >= 30:
            self.animationCounter3 += 1
            if self.speed[0] is not 0:
                self.position[0] += self.speed[0]
            if self.speed[1] is not 0:
                self.position[1] += self.speed[1]
            if self.animationCounter3 > 2:
                if self.speed[0] is not 0 or self.speed[1] is not 0:
                    self.set_image()
                    self.animationCounter3 = 0
            self.moveTime = 0
        self.charGroup.empty()
        self.charGroup.add(self.set_sprite(sprite, screen_size))
#        self.charGroup.add(self.healthBar(screen_size))
        return self.charGroup
    
#    def healthBar(self, screen_size):
#        sprite  = pygame.sprite.Sprite()
#        rect    = pygame.Rect(0,screen_size[1]-50, 150, 100)
#        surface = pygame.Surface((rect.width, rect.height))
##        surface.set_colorkey((0,0,0))
#        pygame.draw.rect(surface, (0,255,0), rect)
#        
#        sprite.image = surface
#        sprite.rect  = rect
#        return sprite
    
    def set_image(self):
        if self.speed[0] > 0:
            self.animationCounter2 = 6
        if self.speed[0] < 0:
            self.animationCounter2 = 3
        if self.speed[1] > 0:
            self.animationCounter2 = 0
        if self.speed[1] < 0:
            self.animationCounter2 = 9
        self.image = self.charElements[self.animationCounter+self.animationCounter2]
        self.animationCounter += 1
        if self.animationCounter == 3: self.animationCounter = 0
        
    def set_sprite(self, sprite, screen_size):
        sprite.image = self.image  
        sprite.rect = sprite.image.get_rect()
        position = list(screen_size)
        position[0] *= 0.5
        position[1] *= 0.5
        position[0] -= (sprite.image.get_rect()[2]*0.5)
        position[1] -= (sprite.image.get_rect()[3]*0.5)
        self.position = position
#        position[0] -= sprite.image.get_rect()[0]
#        position[1] -= sprite.rect.topleft[1]
        sprite.rect = sprite.rect.move(self.position)
        return sprite        
        
    def load_elements(self, path):
        for element in os.listdir(path):
            name = int(element[:-4])
            element = os.path.join(path, element)
            element = pygame.image.load(element)
            self.charElements[name] = element
        print "Character elements loaded"