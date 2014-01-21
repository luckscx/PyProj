'''
Created on 06/02/2013

@author: Simon
'''
import random, math

class ZombieAI:
    
    def __init__(self):
        self.spawntime = 200
        self.zombiepos = []
        self.zombievektors = []
    def spawnTime(self, totalTime):
        self.spawntime = 10000000.0/totalTime
        if self.spawntime < 200:
            self.spawntime = 200
        return self.spawntime
    
    def spawnPos(self, screenSize):
        random1 = random.randrange(0,2)
        random2 = random.randrange(-1,1)
        if not random2:
            random2 = 1
            
        x_pos = random.randrange(0,screenSize[0])*random2
        y_pos = random.randrange(0,screenSize[1])*random2
        
        random3 = random.randrange(0,2)
        if random1:
            if random3:
                x_pos = screenSize[0]
            else:
                x_pos = 0
        else:
            if random3:
                y_pos = screenSize[0]
            else:
                y_pos = 0
             
        return (x_pos, y_pos)
    
    def setZombie(self, zombiePos):
        zombiePos = list(zombiePos)
        self.zombiepos.append(zombiePos)
        self.zombievektors.append((0,0))
        print self.zombievektors
    
    def move_wasd(self, speed, zombies, cameraMove):
        for zombie in zombies:
            index = zombies.index(zombie)
            if cameraMove[0]:
                self.zombiepos[index][0] -= speed[0]
            if cameraMove[1]:
                self.zombiepos[index][1] -= speed[1]
            zombies[index].rect.topleft = [0,0]
            zombies[index].rect = zombies[index].rect.move(self.zombiepos[index])
        return zombies
    
    def move(self, zombies, charPos, tick):
        for zombie in zombies:
            index = zombies.index(zombie)
            position = zombie.rect.topleft        
            try:
                direction = ( charPos[0] - position[0], charPos[1] - position[1] )
                placeholder = math.sqrt(math.pow(direction[0], 2)+math.pow(direction[1], 2))
                e_vektor = (direction[0]/placeholder, direction[1]/placeholder)
            except:
                e_vektor = (1,0)
            self.zombievektors[index] = (e_vektor[0]*-1,e_vektor[1]*-1)
            self.zombiepos[index][0] -= self.zombievektors[index][0]*100*(tick/1000.0)
            self.zombiepos[index][1] -= self.zombievektors[index][1]*100*(tick/1000.0)
            zombies[index].rect.topleft = [0,0]
            zombies[index].rect = zombies[index].rect.move(self.zombiepos[index])
        return zombies