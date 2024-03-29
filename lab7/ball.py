import pygame
import sys

pygame.init()

# размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# размеры и начальное положение мяча
BALL_SIZE = 50
BALL_RADIUS = BALL_SIZE // 2
ball_x = (SCREEN_WIDTH - BALL_SIZE) // 2
ball_y = (SCREEN_HEIGHT - BALL_SIZE) // 2

BALL_SPEED = 20

# создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("мячик")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_y -= BALL_SPEED
    elif keys[pygame.K_DOWN]:
        ball_y += BALL_SPEED
    elif keys[pygame.K_LEFT]:
        ball_x -= BALL_SPEED
    elif keys[pygame.K_RIGHT]:
        ball_x += BALL_SPEED

    # чтобы мяч не вышел за границы экрана
    ball_x = max(0, min(SCREEN_WIDTH - BALL_SIZE, ball_x))
    ball_y = max(0, min(SCREEN_HEIGHT - BALL_SIZE, ball_y))

    # заполнение экрана белым цветом
    screen.fill(WHITE)

    # рисование мяча
    pygame.draw.circle(screen, RED, (ball_x + BALL_RADIUS, ball_y + BALL_RADIUS), BALL_RADIUS)

    # обновление экрана
    pygame.display.flip()

    # ограничение fps
    clock.tick(60)


pygame.quit()
sys.exit()