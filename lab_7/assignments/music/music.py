import pygame 

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 480))

COLOR_WHITE = (255, 255, 255)

# pygame.mixer.music.load('happy.mp3')
# pygame.mixer.music.play(0)

_songs = ['happy.mp3', 'jas_jurek.mp3', 'qanat_jaia.mp3', 'fur_elise.mp3', 'divenire.mp3', 'just_the_two_of_us.mp3']


def next_song(): # function for next_song
    global _songs
    _songs = _songs[1:] + [_songs[0]] # putting current song to the back of the list
    pygame.mixer.music.load(_songs[0]) # loading the next song 
    pygame.mixer.music.play() # playing the loaded song

def previous_song():
    global _songs
    _songs = [_songs[-1]] + _songs[:-1] # putting the last-played song to the front of the list
    pygame.mixer.music.load(_songs[0]) # loading the last-played song
    pygame.mixer.music.play() # playing the loaded song

paused = False

def stopping(): # function for stopping the song
    global paused
    paused = not paused
    if paused:
        pygame.mixer.music.pause() # if the paused it True, call the pause() function 
    else:
        pygame.mixer.music.unpause() # if the paused is False, call unpause() function 

clock = pygame.time.Clock()
FPS = 60

pygame.mixer.music.load(_songs[0]) # loading the current song 
pygame.mixer.music.play() # playing the loaded 'current' song right after the window opens

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: # next song
                next_song() # calling next_song function
            if event.key == pygame.K_LEFT: # previous song
                previous_song() # calling the previous_song function 
            if event.key == pygame.K_SPACE:
                stopping() # calling the stopping() function 

    screen.fill(COLOR_WHITE) # filling the screen with white color

    pygame.display.flip()
    clock.tick(FPS)