

import pygame
from pygame.locals import *
from math import *
from gameobjects.vector3 import Vector3


class main (object):
    def __init__(self):
        self.SCREEN_SIZE = (1200,600)
        self.points = []
        self.scaneSize = 100
        self.resolution = 5
        self.fov = 90
        self.d = self.distance(self.fov,self.SCREEN_SIZE[0])
        pygame.init()
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE,0)
        self.ball = pygame.image.load("ball.png").convert_alpha()
        self.createScenes()
        self.cameraPos = (0,0,-100)

    def distance(self,fov,width):
        d = (width/2)/tan(fov/2)
        return d
    def sortZ(self,point):
        return point[2]
        
        
    def createScenes(self):
        for x in range (-self.scaneSize,self.scaneSize,self.resolution):

            for y in range (-self.scaneSize,self.scaneSize,self.resolution):

                for z in range (-self.scaneSize,self.scaneSize,self.resolution):
                    if sqrt(x**2+y**2+z**2)<40:
                        self.points.append((x,y,z))
        self.points.sort(key=self.sortZ,reverse = True)

    def draw (self):
        
        for point in self.points:
            cameraPointX = point[0]-self.cameraPos[0]
            cameraPointY = point[1]-self.cameraPos[1]
            cameraPointZ = point[2]-self.cameraPos[2]
            if cameraPointZ>0:
                projectX = cameraPointX*self.d/cameraPointZ+self.SCREEN_SIZE[0]/2
                projectY = -cameraPointY*self.d/cameraPointZ+self.SCREEN_SIZE[1]/2
                self.screen.blit(self.ball,(projectX,projectY))

    def run (self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_LEFT] :
                self.cameraPos = (self.cameraPos[0]-0.05,self.cameraPos[1],self.cameraPos[2])
            if pressed_keys[K_RIGHT] :
                self.cameraPos = (self.cameraPos[0]+0.05,self.cameraPos[1],self.cameraPos[2])
            if pressed_keys[K_UP] :
                self.cameraPos = (self.cameraPos[0],self.cameraPos[1],self.cameraPos[2]+0.05)
            if pressed_keys[K_DOWN] :
                self.cameraPos = (self.cameraPos[0],self.cameraPos[1],self.cameraPos[2]-0.05)
            if pressed_keys[K_w] :
                self.cameraPos = (self.cameraPos[0],self.cameraPos[1]+0.05,self.cameraPos[2])
            if pressed_keys[K_s] :
                self.cameraPos = (self.cameraPos[0],self.cameraPos[1]-0.05,self.cameraPos[2])

                

            
            
                
            
            self.screen.fill((0,0,0))
            self.draw()
            pygame.display.update()

myGame = main()
myGame.run()
            
    
                    
