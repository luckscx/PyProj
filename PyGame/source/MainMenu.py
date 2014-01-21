'''
Created on 07/02/2013

@author: Simon
'''
#from zModule import * #includes pygame, os, sys and pygame.locals
import pygame, os
import sys

class MainMenu:

    def __init__(self):
        pathWork = os.getcwd()
        pathMenu  = os.path.join(pathWork, os.path.join("images","menu"))
        self.pathPapers = os.path.join(pathMenu, "papers")
        self.background = pygame.image.load(os.path.join(pathMenu, "background.png"))

        self.Clock = pygame.time.Clock()
        self.timer = 0
        self.aniTimer = 0
        self.aniRunning = True
        
        self.menuItems = {}
        self.current = 0
        self.following = 1
        self.sprites = pygame.sprite.RenderUpdates()
#        self.set_items()
        self.initiative = True
        self.screenSize = (0,0)
        print "Finished initializing MainMenu..."
    
    def controller(self, screen, event):
        screenSize = screen.get_size()
        tick = self.Clock.tick()
        self.timer += tick
        updates = []
        if self.initiative:
            self.menuItems[0].rect.topleft = [0,0]
            self.menuItems[0].rect = self.menuItems[0].rect.move(screenSize[0]*0.5-self.menuItems[0].rect.width*0.5,screenSize[1]*0.06)
            self.sprites.add(self.menuItems[0])
            self.sprites.clear(screen, self.bg)
            updates += self.sprites.draw(screen)
            self.initiative = False
        if self.aniRunning and self.timer >= 2000:
            self.animation(tick, screenSize, self.current, self.following)
        self.sprites.add(self.menuItems[self.current])
        self.sprites.add(self.menuItems[self.following])
        self.sprites.clear(screen, self.bg)
        updates += self.sprites.draw(screen)

        pygame.display.update(updates)
        return screen
    
    def set_items(self, screenSize = (800,600)):
        self.sprites.empty()
        counter = 0
        for element in os.listdir(self.pathPapers):
            path = os.path.join(self.pathPapers, element)
            element = pygame.image.load(path)
            size = element.get_size()
            ratio = size[0]/float(size[1])
            height = int(screenSize[1]-(screenSize[1]*0.1))
            width = int(height * ratio)
            element = pygame.transform.smoothscale(element, (width, height))
            sprite = pygame.sprite.Sprite()
            sprite.image = element
            sprite.rect = sprite.image.get_rect()
            try:
                ratio2 = (self.menuItems[counter].rect[0]+self.screenSize[0])/float(self.menuItems[counter].rect[0])
                sprite.rect[0] = screenSize[0]/ratio2
                sprite.rect[1] = screenSize[1]*0.06
            except:
                print "error"
                sprite.rect = sprite.rect.move(screenSize[0],screenSize[1]*0.06)
            self.menuItems[counter] = sprite
            counter += 1
#        self.initiative = True
        self.screenSize = screenSize

    def animation(self, tick, screenSize, current, following):
        curSprite = self.menuItems[current]
        folSprite = self.menuItems[following]
        curSprite.rect = curSprite.rect.move(-screenSize[0]*3*(tick/1000.0), 0)
        folSprite.rect = folSprite.rect.move(-screenSize[0]*3*(tick/1000.0), 0)
        self.menuItems[current] = curSprite
        self.menuItems[following] = folSprite
        left  = folSprite.rect.topleft[0]
        width = folSprite.rect.width
        if left <= (screenSize[0]*0.5)-(width*0.5):
            folSprite.rect = folSprite.rect.move((left-(screenSize[0]*0.5-width*0.5))*-1,0)
            self.aniRunning = False
        
    
    
    
    
    
    
    
    
    
    
    
    
    def set_background(self, screen, refresh=False):
        if refresh:
            size = screen.get_size()
            print size
            self.bg = pygame.transform.smoothscale(self.background, size)
            screen.blit(self.bg, (0,0))
            return screen
        try:
            self.bg
            return True
        except:
            size = screen.get_size()
            self.bg = pygame.transform.smoothscale(self.background, size)
            return False
    
    
    
#    def controller(self, screen, event):
#        pygame.mouse.set_visible(True)
#        screenSize = list(screen.get_size())
#        size = list(self.background.get_size())
#        if screenSize[0] != size[0] or screenSize[1] != size[1]:
#            self.bgresize = pygame.transform.smoothscale(self.background, screenSize)
#        screen.blit(self.bgresize, (0,0))
#        screen = self.draw_paper(screen)
#        return screen 
#    
#    def draw_paper(self, screen):
#        screenSize = list(screen.get_size())
#        size = list(self.texture1.get_size())
#        if size[1] != int(screenSize[1]*0.7):
#            y = int(screenSize[1]*0.7)
#            ratio = float(size[0]*0.7)/size[1]
#            x = size[0]*ratio
#            self.tx1resize = pygame.transform.smoothscale(self.texture1, (x,y))
#        size = list(self.tx1resize.get_size())
#        halfsize = [size[0]*0.5, size[1]*0.5]
#        mid = [screenSize[0]*0.5 - halfsize[0], screenSize[1]*0.5 - halfsize[1]]
#        screen.blit(self.tx1resize, (mid))
#        return screen