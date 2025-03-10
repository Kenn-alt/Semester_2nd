# Game Components
# • Game Window
# • Game Loop
# • Event Loop(Keyboard press, mouse movements, 'close' button, etc.)

import pygame

pygame.init() # initializes all the pygame sub-modules

screen = pygame.display.set_mode((800, 480)) # creating a game window
# set_mode() takes a tuple as an argument


running = True
while running: # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            # or
            # pygame.quit()

