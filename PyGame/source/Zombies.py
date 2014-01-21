'''
Created on 05/02/2013

@author: Simon
'''
import pygame,os,SpriteSheet,ZombieAI

class Zombies:

    def __init__(self):
        self.ZombieAI = ZombieAI.ZombieAI()
        
        pathWork = os.getcwd()
        pathZombie = os.path.join(pathWork, os.path.join("images", "zombies"))
        self.zombieElements = []
        self.loadElements(pathZombie)
        self.zombies = []
        self.zombieState = []
        self.zombiegroup = pygame.sprite.RenderUpdates()
        self.animationCounter = 0
        
        self.Clock = pygame.time.Clock()
        self.spawnTime = 2000
        self.stateTime = 0
        self.totalTime = 0
        self.moveTime = 0
        print "Finished initiating Zombies module..."
        
    def movement(self, speed, tick, cameraMove):
        self.moveTime += tick
        if self.moveTime >= 30:
            self.zombies = self.ZombieAI.move_wasd(speed, self.zombies, cameraMove)
            self.moveTime = 0
        
    def controller(self, screenSize, charPos):
        tick = self.Clock.tick()
        self.spawnTime += tick
        self.stateTime += tick
        self.totalTime += tick
#        if self.stateTime > 100:
#            self.set_state()
#            self.stateTime = 0
        if self.spawnTime > self.ZombieAI.spawnTime(self.totalTime):
            pos = self.ZombieAI.spawnPos(screenSize)
            self.addZombie(pos)
            self.spawnTime = 0
        if self.zombiegroup:
            self.zombies = self.ZombieAI.move(self.zombies, charPos, tick)
        self.zombiegroup.empty()
        self.zombiegroup.add(self.zombies)
        return self.zombiegroup
    
    def set_state(self):
        for speed in self.ZombieAI.zombievektors:
            dx, dy = speed
            index = self.ZombieAI.zombievektors.index(speed)
            if dy > 0:
                if dx < 0: dx2 = dx*-1
                else: dx2 = dx
                if dy > dx2:
                    animationCounter2 = 12
                elif dx < 0:
                    animationCounter2 = 4
                else:
                    animationCounter2 = 8
            else:
                dy *=-1
                if dx < 0: dx2 = dx*-1
                else: dx2 = dx
                if dy > dx2:
                    animationCounter2 = 0
                elif dx < 0:
                    animationCounter2 = 4
                else:
                    animationCounter2 = 8          
            self.zombies[index].image = self.zombieElements[self.animationCounter+animationCounter2]
            self.animationCounter += 1
            if self.animationCounter == 4: self.animationCounter = 0
    
    def addZombie(self, pos):
        sprite = pygame.sprite.Sprite()
        sprite.image = self.zombieElements[0]
        sprite.rect = sprite.image.get_rect()
        sprite.rect = sprite.rect.move(pos)
        self.zombies.append(sprite)
        self.zombieState.append(0)
        self.ZombieAI.setZombie(sprite.rect.topleft)
    
    def loadElements(self, path):
        self.zombieElements = SpriteSheet.spritesheet(os.path.join(path,"0.png"))
        rects = []
        for n in range(0,5):
            top = 40*n
            for i in range(0,5):
                left = 40*i
                width = 40
                height = 56
                rects.append(pygame.Rect(left, top, width, height))
        self.zombieElements = self.zombieElements.images_at(rects, (0,0,0))
        print "Zombie elements loaded"
        
        
        