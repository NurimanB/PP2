import pygame
import os

# Initialize pygame
pygame.init()

# Set up display
screen_width = 375
screen_height = 812
screen = pygame.display.set_mode((screen_width, screen_height))

# Load iPhone screen image
iphone_img = pygame.image.load('D:\VsCode\python\lab7\player\img/phone.jpeg')
iphone_img = pygame.transform.scale(iphone_img, (screen_width, screen_height))

# Set the directory where your music files are located
music_dir = 'D:\VsCode\python\lab7\player\songs'

# Get a list of all music files in the directory
music_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]

# Initialize variables 
current_track = 0
paused = False

# Load the first track
pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))

# Play the loaded track
pygame.mixer.music.play()

# Font
font = pygame.font.SysFont(None, 30) 

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
                pygame.mixer.music.play()

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw iPhone screen
    screen.blit(iphone_img, (0, 0))


    # Display music name
    music_name = music_files[current_track].split('.')[0]
    text = font.render(music_name, True, (0, 0, 0))
    text_rect = text.get_rect(center=(screen_width // 2, 510))
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
