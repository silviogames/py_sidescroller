from random import randint
import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("jump test")
vec = pygame.math.Vector2
x = 50
y = 50
width = 40
height = 60
vel = 5
clock = pygame.time.Clock()
global run
run = True
delta = 0

class gameobj:
    def __init__(self,x,y):
        self.pos = vec(x,y) 
        self.color = (randint(0,255),randint(0,255),randint(0,255))
        self.vel = vec(30,30);

    def render(self,surf):
        pygame.draw.circle(surf, self.color, (int(self.pos.x),int( self.pos.y)), 20)
    
    def update(self,dt):
        self.pos = self.pos + self.vel * dt; 
        # wall collision
        if self.pos.x < 0 or self.pos.x > 500:
            self.vel.x = -self.vel.x

        if self.pos.y < 0 or self.pos.y > 500:
            self.vel.y = -self.vel.y
            
b = gameobj(10,10)
c = gameobj(100,100)
list_boxes = [b,c]

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                list_boxes.append(gameobj(randint(0,500), randint(0,500)))
            if event.key == pygame.K_ESCAPE:
                return False 
    return True

def update(dt):
    for b in list_boxes:
        b.update(dt)

def render():
    for b in list_boxes:
        b.render(win)
        
while handle_input():
    win.fill((20,20,20))
    render()
    pygame.display.update()
    dt = clock.tick(60)
    update(float(dt) / 1000)
pygame.quit()
print("game closed")

