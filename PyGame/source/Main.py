'''
Created on 02/02/2013

@author: Simon
'''
import PyHandler, pygame, sys, MainMenu
from pygame.locals import *
import profile

class Main:
    
    def __init__(self):
        # Create PyHandler object
        self.Game = PyHandler.Main()
        self.Game.display((800,600))
        
        self.MainMenu = MainMenu.MainMenu()
        
        self.Clock = pygame.time.Clock() #Used to keep a constant frame-rate
        self.framerate = 200              #Frame-rate
        
        self.scene = 1
        
    
    def main_loop(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    print pygame.mouse.get_pos()
                elif event.type == VIDEORESIZE:
                    if self.scene == 0:
                        self.Game.update(event.size)
                        self.Game.screen = self.MainMenu.set_background(self.Game.screen, True)
                        self.MainMenu.set_items(event.size)
                        pygame.display.flip()
                    if self.scene == 1:
                        self.Game.display(event.size)
            self.Clock.tick(self.framerate)
            fps = self.Clock.get_fps()
            if self.scene == 0:
                self.Game.screen = self.MainMenu.controller(self.Game.screen, events)
            if self.scene == 1:
                self.Game.controller(fps, events)

if __name__ == '__main__':
    MainObject = Main()
    try:
        profile.run('MainObject.main_loop()')
    except:
        # Runs the main loop
        MainObject.main_loop()
