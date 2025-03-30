import pygame, math
from color_palette import *

pygame.init()

WIDTH = 800
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.Font('game_bubble.ttf', 15)
e_key_message = font.render("Press 'E' to erase", True, COLOR_BLACK)
d_key_message = font.render("Press D to draw", True, COLOR_BLACK)
circle_message = font.render('Press 1 to draw Circle', True, COLOR_BLACK)
rect_message = font.render('Press 2 to draw Rect', True, COLOR_BLACK)
color_green_message = font.render('Press 3 for Green', True, COLOR_BLACK)
color_blue_message = font.render('Press 4 for Blue', True, COLOR_BLACK)
color_purple_message = font.render('Press 5 for Purple', True, COLOR_BLACK)

base_layer = pygame.Surface((WIDTH, HEIGHT))

LMB_pressed = False
THICKNESS = 5
eraser_thickness = 50

mode = 'circle'
color = colors[0]

curr_x = 0
curr_y = 0
prev_x = 0
prev_y = 0

center = (0, 0)
radius = 0

clock = pygame.time.Clock()
FPS = 60

def radius(x1, y1, x2, y2):
    return int(math.sqrt((x1 - x2)**2 + (y1 - y2)**2)) // 2 # getting the radius 

def center(x1, y1, x2, y2):
    return ((x1 + x2) // 2, (y1 + y2) // 2) # getting the center of the circle

def calculate_rect(x1, y1, x2, y2): # calculating coords of a rectangle
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

eraser = False

base_layer.fill(COLOR_WHITE)
screen.blit(base_layer, (0, 0))

def draw_menu(): 
    pygame.draw.rect(base_layer, COLOR_GRAY, (0, 0, WIDTH, 70))
    pygame.draw.line(base_layer, COLOR_BLACK, (0, 70), (WIDTH, 70))
    base_layer.blit(e_key_message, (10, 14))
    base_layer.blit(d_key_message, (10, 42))
    base_layer.blit(circle_message, (160, 14))
    base_layer.blit(rect_message, (160, 42))
    base_layer.blit(color_green_message, (350, 14))
    base_layer.blit(color_blue_message, (350, 42))
    base_layer.blit(color_purple_message, (500, 14))

running = True
while running:

    draw_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMB_pressed = True
            prev_x = event.pos[0]
            prev_y = event.pos[1]
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMB_pressed = False
            if not eraser:
                curr_x = event.pos[0]
                curr_y = event.pos[1]
                if mode == 'circle':
                    pygame.draw.circle(base_layer, color, center(curr_x, curr_y, prev_x, prev_y), radius(curr_x, curr_y, prev_x, prev_y), THICKNESS)
                if mode == 'rect':
                    pygame.draw.rect(screen, color, calculate_rect(prev_x, prev_y, curr_x, curr_y), THICKNESS)

            base_layer.blit(screen, (0, 0))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                eraser = True
            if event.key == pygame.K_d:
                eraser = False
            if event.key == pygame.K_1:
                mode = 'circle'
            if event.key == pygame.K_2:
                mode = 'rect'
            if event.key == pygame.K_3:
                color = colors[0]
            if event.key == pygame.K_4:
                color = colors[1]
            if event.key == pygame.K_5:
                color = colors[2]
            
        screen.blit(base_layer, (0, 0))

        if event.type == pygame.MOUSEMOTION:
            if LMB_pressed:
                if eraser:
                    curr_x = event.pos[0] # we need the positions of both 'curr' and 'prev'
                    curr_y = event.pos[1] # because we need to draw the 'eraser' line from the position 
                    prev_x = event.pos[0] # when of 'curr' to 'prev'
                    prev_y = event.pos[1] # if we remove curr_x, curr_y, then the line will be drawn starting from the last position of the last created line
                    # if we remove the curr_x, curr_y, we won't follow our mouse in the MOUSEMOTION event
                    # if we remove the prev_x, prev_y, we will infinite lines with prev_x, prev_y in the position of a pressed button and curr_x, curr_y wherever the mouse is while MOUSEMOTION
                    pygame.draw.line(base_layer, COLOR_WHITE, (prev_x, prev_y), (curr_x, curr_y), eraser_thickness)
                elif not eraser:
                    curr_x = event.pos[0] 
                    curr_y = event.pos[1]
                    if mode == 'circle':
                        pygame.draw.circle(screen, color, center(curr_x, curr_y, prev_x, prev_y), radius(curr_x, curr_y, prev_x, prev_y), THICKNESS)
                    if mode == 'rect':
                        pygame.draw.rect(screen, color, calculate_rect(prev_x, prev_y, curr_x, curr_y), THICKNESS)

    pygame.display.flip()
    clock.tick(FPS)
