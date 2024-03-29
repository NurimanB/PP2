import pygame
import os

pygame.init()

screen_width = 375
screen_height = 812
screen = pygame.display.set_mode((screen_width, screen_height))

iphone_img = pygame.image.load('D:\VsCode\python\lab7\player\img/phone.jpeg')
iphone_img = pygame.transform.scale(iphone_img, (screen_width, screen_height))

music_dir = 'D:\VsCode\python\lab7\player\songs'

music_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]

current_track = 0
paused = False

pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))

pygame.mixer.music.play()

font = pygame.font.SysFont(None, 30) 

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

    screen.fill((255, 255, 255))
    screen.blit(iphone_img, (0, 0))

    music_name = music_files[current_track].split('.')[0]
    text = font.render(music_name, True, (0, 0, 0))
    text_rect = text.get_rect(center=(screen_width // 2, 510))
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
