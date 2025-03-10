import pygame

pygame.init()

screen = pygame.display.set_mode((800, 480))

running = True
while running: 
    for event in pygame.event.get():
        print(event) # printing all the events 
        if event.type == pygame.QUIT:
            running = False

            