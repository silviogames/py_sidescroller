# this file handles game entites like the player, enemies or items
from random import randint
import pygame
import gamemap
vec = pygame.math.Vector2

class entity:
    def __init__(self,x,y,world):
        self.pos = vec(x,y) 
        self.dead = False
        self.world = world
        self.vel = vec(randint(-100, 100),randint(-100, 100));
        
    def render(self,surf):
        pass
    
    def collision(self):
        # tilemap box collision
        return self.world.collision(self.pos.x, self.pos.y) 
    
    def update(self,dt):
        self.pos = self.pos + self.vel * dt; 
        

class Ball(entity):
    def __init__(self,x,y,radius,world):
        entity.__init__(self,x,y,world)
        self.radius = radius
        self.color = (randint(0,255),randint(0,255),randint(0,255))

    def update(self,dt):
        super().update(dt)
        if self.collision() == True:
            # set radius down
            self.radius-=1
            if self.radius < 1:
                self.dead = True

    def render(self,surf):
        pygame.draw.circle(surf, self.color, (int(self.pos.x),int( self.pos.y)), self.radius)

class Box(entity):
    def __init__(self,x,y,world):
        entity.__init__(self,x,y,world)
        self.color = (randint(0,255),randint(0,255),randint(0,255))
        self.width = 10
        self.height = 10

    def update(self,dt):
        super().update(dt)
        if self.collision() == True:
            print("box collision")

    def render(self,surf):
        pygame.draw.rect(surf,self.color, (self.pos.x, self.pos.y, self.width, self.height))

