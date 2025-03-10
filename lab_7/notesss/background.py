import pygame 

pygame.init()

screen = pygame.display.set_mode((800, 480))

COLOR_RED = (255, 0, 0) # Color 'red' in RGB
# each color component has a value between 0 and 255(overall 256 -> 8 bits)
# Total: 24 bits 

COLOR_BLUE = (0, 0, 255)

running = True
is_red = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_red = not is_red # flipping the colors

    if is_red:
        screen.fill(COLOR_RED) # filling the background with some color
    else:
        screen.fill(COLOR_BLUE)
    

    pygame.display.flip() # updates the screen

