import pygame
from color_palette import *

pygame.init()

WIDTH = 800
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))

LMB_pressed = False # for storing boolean of whether Left Mouse Button is pressed 
THICKNESS = 5

square_mode = False
triangle_right_mode = False
triangle_equilateral_mode = False

mouse_x, mouse_y = pygame.mouse.get_pos() # getting the position of the mouse

curr_x = mouse_x
curr_y = mouse_y

prev_x = mouse_x
prev_y = mouse_y

def calculate_rect(x1, x2, y1, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def square():
    global LMB_pressed, curr_x, curr_y, prev_x, prev_y
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        prev_x = event.pos[0]
        prev_y = event.pos[1]
        ############################### I was there 

    # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    #     LMB_pressed = True
    #     curr_x = event.pos[0]
    #     curr_y = event.pos[1]
    # if event.type == pygame.MOUSEMOTION:
    #     curr_x = event.pos[0]
    #     curr_y = event.pos[1]
    # if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
    #     LMB_pressed = False
    #     pygame.draw.line(screen, COLOR_BLUE, (prev_x, prev_y), (curr_x, curr_y), THICKNESS)

def triangle_right():
    pass

def triangle_equilateral():
    pass

def rhombus():
    pass

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #     LMB_pressed = True
        #     # curr_x = event.pos[0]
        #     # curr_y = event.pos[1]
        #     prev_x = event.pos[0]
        #     prev_y = event.pos[1]
        # if event.type == pygame.MOUSEMOTION:
        #     curr_x = event.pos[0]
        #     curr_y = event.pos[1]
        #     pygame.draw.line(screen, COLOR_BLUE, (prev_x, prev_y), (curr_x, curr_y), THICKNESS)
        # if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        #     LMB_pressed = False
        #     pygame.draw.line(screen, COLOR_BLUE, (prev_x, prev_y), (curr_x, curr_y), THICKNESS)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                THICKNESS -= 1
            if event.key == pygame.K_1: # If the user presses '1', the Square mode turns on
                square_mode = True
            if event.key == pygame.K_2: # If the user presses '2', the Right Triangle mode turns on 
                triangle_right_mode = True
            if event.key == pygame.K_3: # If the user presses '2', the Right Triangle mode turns on 
                triangle_equilateral_mode = True
            if event.key == pygame.K_4: # If the user presses '2', the Right Triangle mode turns on 
                rhombus_mode = True
        if square_mode:
            square()
        if triangle_right_mode:
            triangle_right()
        if triangle_right_mode:
            triangle_right()
        if rhombus_mode:
            rhombus()

    # if LMB_pressed:
    #     pygame.draw.line(screen, COLOR_BLUE, (prev_x, prev_y), (curr_x, curr_y), THICKNESS)
        # this line above makes sure that we draw a line while we're moving our mouse

    # prev_x = curr_x # we need to update our previous coords with the current, 
    # prev_y = curr_y # so that every iteration, we follow our mouse MOTION

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()