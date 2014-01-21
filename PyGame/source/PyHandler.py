'''
Created on 02/02/2013

@author: Simon
'''
import pygame, os, math, Character, Shots, Zombies, Objects, Camera
from pygame.locals import *
pygame.init()

class Main:

    def __init__(self):
        pathWork = os.getcwd()
        pathImg  = os.path.join(pathWork, "images")
        background = os.path.join(pathImg, "bg.jpg")
        self.background = pygame.image.load(background)
        self.View = Camera.View()
        self.bg = self.View.bgCropped
        self.myFont = pygame.font.SysFont("Calibri", 14)
        
        self.fpsSprite = pygame.sprite.Sprite()
        self.killSprite = pygame.sprite.Sprite()
        self.group = pygame.sprite.RenderUpdates(self.fpsSprite, self.killSprite)
        self.Clock = pygame.time.Clock()
        self.fpsTime = 0
        
        self.Character = Character.Character()
        self.charSprite = pygame.sprite.Sprite()
        self.charGroup = pygame.sprite.RenderUpdates(self.charSprite)
        self.kills = 0
        
        self.shooting = False
        self.mouse = (0,0)
        self.Shoot = Shots.Shoot()
        self.shotsGroup = pygame.sprite.RenderUpdates()
        
        self.Zombies = Zombies.Zombies()
        self.zombieGroup = pygame.sprite.RenderUpdates()
        
        self.Objects = Objects.Objects()
        self.objectgroup = pygame.sprite.RenderUpdates()
        
        self.moveTime = 0
    
        # Cursor skal loades igennem weapons modulet, naar det er lavet
        # da det skal skifte udseende afhaengigt at vaaben
        self.mouseSprite = pygame.sprite.Sprite()
        self.mouseSprite.image = pygame.image.load(os.path.join(pathImg, "crosshair.png"))
        self.mouseGroup = pygame.sprite.RenderUpdates(self.mouseSprite)
        
    def controller(self, fps, events):
        pygame.mouse.set_visible(False)
        updates = []
        self.collisionDetection()
        self.checkEvents(events)
        loopTime = self.Clock.tick()
#        if not self.arena:
#            self.create_arena()
#        updates += self.updateHouseSprite(events)
        updates += self.set_background(events)
        updates += self.updateCharSprite(events)
        updates += self.updateShootSprite(events)
        updates += self.updateZombieSprite()
        updates += self.tempCrossHair()
        updates += self.stats(fps)
        pygame.display.update(updates)
      
    def updateHouseSprite(self, events):
        self.objectgroup.clear(self.screen, self.bg)
        self.objectgroup = self.Objects.controller(events, self.screen.get_size())
        if self.objectgroup:
            update = self.objectgroup.draw(self.screen)
            return update 
        return [] 
        
    def updateCharSprite(self, events):
        self.charGroup.clear(self.screen, self.bg)
        self.charGroup = self.Character.controller(events, self.screen.get_size(), self.charSprite)
        update = self.charGroup.draw(self.screen)
        return update
    
    def updateShootSprite(self, event):
        self.shotsGroup.clear(self.screen, self.bg)
        self.shotsGroup = self.Shoot.controller(self.screen.get_size(), self.charSprite.rect.topleft, pygame.mouse.get_pos(), self.shooting)
        update = self.shotsGroup.draw(self.screen)
        return update
        
    def updateZombieSprite(self):
        self.zombieGroup.clear(self.screen, self.bg)
        self.zombieGroup = self.Zombies.controller(self.screen.get_size(), self.Character.position)
        update = self.zombieGroup.draw(self.screen)
        return update   
        
    def checkEvents(self, events):
        for event in events:
            if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:  
                self.shooting = True
                self.mouse = pygame.mouse.get_pos()
            elif event.type == MOUSEBUTTONUP:
                self.shooting = False      
        
    def collisionDetection(self):
        collision = pygame.sprite.groupcollide(self.zombieGroup, self.shotsGroup, 0, 0)   
        for zombie in collision.keys():
            self.kills += 1
            number = self.Zombies.zombies.index(zombie)
            self.Zombies.zombies.pop(number)
            self.Zombies.ZombieAI.zombiepos.pop(number)
            self.Zombies.ZombieAI.zombievektors.pop(number)
        for shots in collision.values():
            for shot in shots:
                try:
                    number = self.Shoot.shotslist.index(shot)
                    self.Shoot.shotslist.pop(number)
                    self.Shoot.directions.pop(number)
                    self.Shoot.topleft.pop(number)
                except:
                    print "Collision detecting should be changed if this error occurs often"
        collision = pygame.sprite.groupcollide(self.zombieGroup, self.charGroup, 0, 0)
        for zombie in collision.keys():
            print "A zombie can hit you now! - This feature will be added later"
                        
    def tempCrossHair(self):
        self.mouseGroup.clear(self.screen, self.bg)
        self.mouseSprite.rect = self.mouseSprite.image.get_rect()
        self.mouseSprite.rect.topleft = [0,0]
        topleft = pygame.mouse.get_pos()
        topleft = (topleft[0]-10, topleft[1]-10)
        self.mouseSprite.rect = self.mouseSprite.rect.move(topleft)
        update = self.mouseGroup.draw(self.screen)
        return update
        
        
    def set_background(self, events):
        self.moveTime += self.View.tick
        update = self.View.controller(events)
        if update != False:
            if type(update) != list:
                update = [update]
            self.bg = self.View.bgCropped
            self.screen.blit(self.bg, (0,0))
            #move zombies
            cameraMove = (self.View.cameradx,self.View.camerady)
            self.Zombies.movement(self.View.speed, self.moveTime, cameraMove)
            self.moveTime = 0
            return update
        return []
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def stats(self, fps):
        self.group.clear(self.screen, self.bg)
        fps = "%.2f" % fps
        text = self.myFont.render("FPS: "+fps, 1, (255,255,0))
        self.fpsSprite.image = text
        self.fpsSprite.rect = self.fpsSprite.image.get_rect()
        self.fpsSprite.rect.topleft = [2, 2]
        kills = str(self.kills)
        text2 = self.myFont.render("Kills: "+kills, 1, (255,255,0))
        self.killSprite.image = text2
        self.killSprite.rect = self.killSprite.image.get_rect()
        self.killSprite.rect.topleft = [2, 20]
        update = self.group.draw(self.screen)
        return update
            
    def create_arena(self):
        screen_size = self.screen.get_size()
        surface = pygame.Surface(screen_size)
        bg_size = self.background.get_size()
        x_no = screen_size[0] / float(bg_size[0])
        y_no = screen_size[1] / float(bg_size[1])
        x_no = int(math.ceil(x_no))
        y_no = int(math.ceil(y_no))
        for y in range(y_no):
            for x in range(x_no):
                position = (x*bg_size[0], y*bg_size[1])
                surface.blit(self.background, position)
        self.bg = surface
        self.screen.blit(self.bg, (0,0))
        self.arena = True
        pygame.display.flip()
    
    def display(self, size, caption="Zombie Shooter - Simon Larsen"):
        self.screen = pygame.display.set_mode(size, RESIZABLE, 32)
        pygame.display.set_caption(caption)
        self.screen.blit(self.bg, (0,0))
        pygame.display.flip()
        self.arena = False
    
    def update(self, size):
        self.screen = pygame.display.set_mode(size, RESIZABLE, 32)
        