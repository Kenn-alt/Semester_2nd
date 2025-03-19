import pygame, random, time

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

image_background = pygame.image.load('/Users/kenn_/my_file/Semester_2nd/lab_8/notesss/AnimatedStreet.png')
image_player = pygame.image.load('/Users/kenn_/my_file/Semester_2nd/lab_8/notesss/Player.png')
image_enemy = pygame.image.load('Enemy.png')

font = pygame.font.SysFont('Verdana', 60)
image_game_over = font.render('Game Over', True, 'black')
image_game_over_rect = image_game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2))

pygame.mixer.music.load('/Users/kenn_/my_file/Semester_2nd/lab_8/notesss/background.wav')
pygame.mixer.music.play(-1) # -1 is for playing infinitely

sound_crash = pygame.mixer.Sound('/Users/kenn_/my_file/Semester_2nd/lab_8/notesss/crash.wav')

# sprite - an object that has a 2D image and coords for this image

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2 # putting the center coordinate of the 'car'
        self.rect.bottom = HEIGHT # putting the coordinate of the bottom line of the 'car' 
        # or 
        # self.rect.midbottom = (WIDTH // 2, HEIGHT) # specifying both of the coordinates of midbottom point
        # of the 'car' 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            # move() function needs to assign a value of the moved image
            # self.rect = self.rect.move(self.speed, 0) # move() function needs to assign a value of the moved image
            self.rect.move_ip(self.speed, 0)  # moveip() ---- move in place ---- function directly changes our self.rect 
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0 # if the left side is less than 0, self.rect.left = 0 
        # if self.rect.x < 0:
        #     self.rect.x = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH # if the right side is greater than WIDTH, self.rect.right = WIDTH 
        # if self.rect.x > WIDTH - self.rect.w: # if self.rect.x(which is the coord. of the topleft of the car)
        #                                       # is greater than (WIDTH - self.rect.w), move it back to the
        #                                       # (WIDTH - self.rect.w) position
            # self.rect.x = WIDTH - self.rect.w

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.speed = 10
        self.rect = self.image.get_rect()

    def generate_random_rect(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()
        


clock = pygame.time.Clock()
FPS = 60

player = Player()
enemy = Enemy()

all_sprites = pygame.sprite.Group() # sprites have Group() class that enables to group sprites to blit() them  
all_sprites.add(player, enemy)      # one-by-one on the screen
enemy_sprites = pygame.sprite.Group()
enemy_sprites.add(enemy)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move()

    screen.blit(image_background, (0, 0))
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        time.sleep(3)
        screen.fill('red')
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()
    

    pygame.display.flip()   
    clock.tick(FPS)
    