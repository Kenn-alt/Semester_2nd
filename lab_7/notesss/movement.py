import pygame

pygame.init()

WIDTH = 1200
HEIGHT = 720

circle_x = WIDTH // 2
circle_y = HEIGHT // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))

COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)

movement_speed = 10

FPS = 60

clock = pygame.time.Clock()

is_red = True
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        circle_y -= movement_speed
    if pressed_keys[pygame.K_DOWN]:
        circle_y += movement_speed
    if pressed_keys[pygame.K_RIGHT]:
        circle_x += movement_speed
    if pressed_keys[pygame.K_LEFT]:
        circle_x -= movement_speed
    if pressed_keys[pygame.K_SPACE]:
        is_red = not is_red
    
    if is_red: 
        screen.fill(COLOR_RED)
        pygame.draw.circle(screen, COLOR_BLUE, (circle_x, circle_y), 50)
    else:
        screen.fill(COLOR_BLUE)
        pygame.draw.circle(screen, COLOR_RED, (circle_x, circle_y), 50)

    pygame.display.update()
    clock.tick(FPS)
