# The terminal must located in the directory where the 'ball.png' is located
# Example: if the terminal is in 'lab_7', and our 'ball.png' is in 'lab_7/notesss' the program
# will be searching for 'ball.png' inside the 'lab_7' directory 

import pygame 

pygame.init()

WIDTH = 800
HEIGHT = 480

screen = pygame.display.set_mode((800, 480))

COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

circle_x = WIDTH // 2
circle_y = HEIGHT // 2

x = 30
y = 30

movement_speed = 5

running = True

font = pygame.font.SysFont('comicsanms', 72) # the arguments are: name of the font, size of the font

text = font.render('Hello, World!', True, COLOR_BLUE) # • the arguments are: the text that will be shown, 
                                                      # • the 'antialias'(сглаживание) argument -> True or False
                                                      # If "antialias" is set to True, the rendered text will have smooth edges.
                                                      # • the color of the text

clock = pygame.time.Clock()
FPS = 60
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_red = not is_red
            
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        y -= movement_speed
    if pressed_keys[pygame.K_DOWN]:
        y += movement_speed
    if pressed_keys[pygame.K_RIGHT]:
        x += movement_speed
    if pressed_keys[pygame.K_LEFT]:
        x -= movement_speed

    screen.fill(COLOR_WHITE)

    screen.blit(text, (x, y)) # blit() function helps to put our image at the (x, y) coordinate

    pygame.display.flip()
    clock.tick(FPS)

