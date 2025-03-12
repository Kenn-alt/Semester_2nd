import pygame 

pygame.init()

WIDTH = 800
HEIGHT = 480

screen = pygame.display.set_mode((800, 480))

COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)

circle_x = WIDTH // 2
circle_y = HEIGHT // 2

movement_speed = 5

running = True
is_red = True

clock = pygame.time.Clock()
FPS = 60
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_red = not is_red
            



    # use get_pressed() function when you need to find what keys are being pressed and the order in which
    # keys are being pressed doesn't matter
    # Otherwise, use the variables 'up_pressed', 'down_pressed', etc. with 'if' statements
    # to recognize the pressed keys
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        circle_y -= movement_speed
    if pressed_keys[pygame.K_DOWN]:
        circle_y += movement_speed
    if pressed_keys[pygame.K_RIGHT]:
        circle_x += movement_speed
    if pressed_keys[pygame.K_LEFT]:
        circle_x -= movement_speed


    if is_red:
        screen.fill(COLOR_BLUE)
        pygame.draw.circle(screen, COLOR_RED, (circle_x, circle_y), 40)
    else:
        screen.fill(COLOR_RED)
        pygame.draw.circle(screen, COLOR_BLUE, (circle_x, circle_y), 40)

    pygame.display.flip()
    clock.tick(FPS)