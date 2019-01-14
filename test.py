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
        self.radius = 20
        self.dead = False
        self.color = (randint(0,255),randint(0,255),randint(0,255))
        self.vel = vec(randint(-100, 100),randint(-100, 100));

    def render(self,surf):
        pygame.draw.circle(surf, self.color, (int(self.pos.x),int( self.pos.y)), self.radius)
    
    def update(self,dt):
        self.pos = self.pos + self.vel * dt; 
        # wall collision
        collision = False
        if self.pos.x < 0 or self.pos.x > 500:
            self.vel.x = -self.vel.x
            collision = True
        if self.pos.y < 0 or self.pos.y > 500:
            self.vel.y = -self.vel.y
            collision = True 
        if collision == True:
            # set radius down
            self.radius-=1
            if self.radius < 1:
                self.dead = True
                self.radius = 1

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
        if b.dead == True:
            list_boxes.remove(b)

def render():
    for b in list_boxes:
        b.render(win)
    for i in range(len(list_boxes)):
       pygame.draw.rect(win, (255,255,255),(10 + (i * 3), 10, 2,5)) 

while handle_input():
    win.fill((20,20,20))
    render()
    pygame.display.update()
    dt = clock.tick(60)
    #limit deltatime to max value to prevent jumping
    update(float(dt) / 1000)
pygame.quit()
print("game closed")

