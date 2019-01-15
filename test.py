from random import randint
import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("jump test")
vec = pygame.math.Vector2
basic_font = pygame.font.Font(None, 20)
clock = pygame.time.Clock()
global run
run = True
delta = 0
color_white = (255, 255, 255)
color_red = (255, 20, 20)

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

list_text_surf = []
list_text_rect = []

def handle_input():
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                list_boxes.append(gameobj(randint(0,500), randint(0,500)))
            if event.key == pygame.K_ESCAPE:
                return False 
    return True

def create_text(message, font, color):
    text_surf = font.render(message, True, color)
    return text_surf, text_surf.get_rect()  
            
def draw_text(message,x,y, color, font):
    text_surf, text_rect = create_text(message, font, color)
    text_rect.x = x
    text_rect.y = y
    list_text_surf.append(text_surf)
    list_text_rect.append(text_rect)

def update(dt):
    for b in list_boxes:
        b.update(dt)
        if b.dead == True:
            list_boxes.remove(b)

def render():
    for b in list_boxes:
        b.render(win)

    draw_text("balls in game " + str(len(list_boxes)),10, 10, color_white, basic_font)   
       
    if len(list_text_rect) != len(list_text_surf):
        print("text list mismatch")
    else:
        for i in range(len(list_text_surf)):
            win.blit(list_text_surf[i], list_text_rect[i])
    list_text_rect.clear()
    list_text_surf.clear()

while handle_input():
    win.fill((20,20,20))
    render()
    pygame.display.update()
    dt = clock.tick(60)
    #limit deltatime to max value to prevent jumping
    update(float(dt) / 1000)
pygame.quit()
print("game closed")

