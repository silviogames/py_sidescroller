from random import randint
import pygame
import utils
import gamemap
import color
import entity
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("jump test")
vec = pygame.math.Vector2
basic_font = pygame.font.Font(None, 20)
clock = pygame.time.Clock()
global run
run = True
delta = 0

game_world = gamemap.world(20,20,15)
game_world.generate()
game_world.add_entity(entity.Ball(10,10,15))

list_text_surf = []
list_text_rect = []

def handle_input():
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                game_world.add_entity(entity.Ball(randint(0,500), randint(0,500),20))
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
    game_world.update(dt) 
        
def render():
    game_world.render(win)

    draw_text("entities in game " + str(len(game_world.entities)),10, 10, color.white, basic_font)   
       
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

