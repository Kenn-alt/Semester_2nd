# Being able draw only vertically or horizontally

import pygame
from color_palette import * 

pygame.init()

WIDTH = 800
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60

THICKNESS = 5

LMB_pressed = False

mode = 'horizontal'

mouse_x, mouse_y = pygame.mouse.get_pos()
prev_x = mouse_x
prev_y = mouse_y
curr_x = mouse_x
curr_y = mouse_y

dx = 0
dy = 0

base_layer = pygame.Surface((WIDTH, HEIGHT))

def draw_horizontal():
    pygame.draw.line(screen, COLOR_GREEN, (prev_x, prev_y), (curr_x, prev_y), THICKNESS)

def draw_vertical():
    pygame.draw.line(screen, COLOR_GREEN, (prev_x, curr_y), (prev_x, prev_y), THICKNESS)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = 'horizontal'
            if event.key == pygame.K_2:
                mode = 'vertical'
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            LMB_pressed = True
            prev_x = event.pos[0]
            prev_y = event.pos[1]
            # curr_x = event.pos[0]
            # curr_y = event.pos[1]
        if event.type == pygame.MOUSEMOTION:
            draw_horizontal()
            curr_x = event.pos[0] # we change current coords and while LMB pressed draw this line
            curr_y = event.pos[1]
            screen.blit(base_layer, (0, 0))
        if event.type == pygame.MOUSEBUTTONUP:
            LMB_pressed = False
            if mode == 'horizontal':
                draw_horizontal()
            if mode == 'vertical':
                draw_vertical()
            base_layer.blit(screen, (0, 0))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            elif event.key == pygame.K_MINUS:
                THICKNESS -= 1

    if LMB_pressed: # the line from previous coords to current is drawn 
        if mode == 'horizontal':
            draw_horizontal()
        if mode == 'vertical':
            draw_vertical()

    # prev_x = curr_x # the current coords become previous for the next iteration 
    # prev_y = curr_y

    pygame.display.flip()
    clock.tick(FPS)