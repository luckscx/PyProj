'''
Created on 04/02/2013

@author: Simon
'''
import os, pygame, math
from pygame.locals import *

class Shoot:

    def __init__(self):
        pathWork = os.getcwd()
        pathImg = os.path.join(pathWork, "images")
        pathProj = os.path.join(pathImg, "projectiles")
        self.projElements = {}
        self.load_elements(pathProj)
        
        self.shots = pygame.sprite.RenderUpdates()
        self.shotslist = []
        self.directions = []
        self.topleft = []
        self.Clock = pygame.time.Clock()
        self.shootTime = 0
        self.positionUpdate = 0
        self.weaponCD = [120]
        print "Finished initiating Shoot module..."        
    
    def controller(self, screenSize, charPos, mousePos, shoot=False, weapon=0):
        tick = self.Clock.tick()
        self.shootTime += tick
        self.positionUpdate += tick
        if shoot:
            if self.shootTime >= self.weaponCD[weapon]:
                self.addShot(weapon, charPos, mousePos)
                self.shootTime = 0
        if self.shots:
            if self.positionUpdate > 10:
                self.update_pos(self.positionUpdate, screenSize)
                self.positionUpdate = 0
        else:
            self.positionUpdate = 0
            
        self.shots.empty()
        self.shots.add(self.shotslist)
        return self.shots
    
    def update_pos(self, deltaTime, screenSize):
        var = 0
        for sprite in self.shotslist:
            topleft = sprite.rect.topleft
            if topleft[0] < -50 or topleft[1] < -50:
                self.shotslist.pop(var)
                self.topleft.pop(var)
                self.directions.pop(var)
            elif topleft[0] > screenSize[0] or topleft[1] > screenSize[1]:
                self.shotslist.pop(var)
                self.topleft.pop(var)
                self.directions.pop(var)
            else:    
                #Hvor 200 er pixel pr. sekund - altsaa skudets hastighed
                self.topleft[var][0] += self.directions[var][0]*400*(deltaTime/1000.0)
                self.topleft[var][1] += self.directions[var][1]*400*(deltaTime/1000.0)
                self.shotslist[var].rect.topleft = [0,0]
                self.shotslist[var].rect = self.shotslist[var].rect.move(self.topleft[var])
            var += 1
    
    def addShot(self, weapon, charPos, mousePos):
        sprite = pygame.sprite.Sprite()
        sprite.image = self.projElements[weapon]
        sprite.rect = sprite.image.get_rect()
        sprite.rect = sprite.rect.move(charPos)
        self.shotslist.append(sprite)
        topleft = sprite.rect.topleft
        topleft = list(topleft)
        self.topleft.append(topleft)
        try:
            direction = ( charPos[0] - mousePos[0], charPos[1] - mousePos[1] )
            placeholder = math.sqrt(math.pow(direction[0], 2)+math.pow(direction[1], 2))
            e_vektor = (direction[0]/placeholder, direction[1]/placeholder)
        except:
            e_vektor = (1,0)
        e_vektor = (e_vektor[0]*-1,e_vektor[1]*-1)
        self.directions.append(e_vektor) 
        return sprite
    
    def load_elements(self, path):
        for element in os.listdir(path):
            name = int(element[:-4])
            element = os.path.join(path, element)
            element = pygame.image.load(element)
            self.projElements[name] = element
        print "Projectile elements loaded"
