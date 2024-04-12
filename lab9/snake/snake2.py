import pygame as pg
from random import randrange
import time

pg.init()

w, h, fps, level, step = 800, 800, 6, 0, 40  # разделяем окно на 400 квадратиков, 20 на 20
screen = pg.display.set_mode((w, h))
pg.display.set_caption('змейка улучшенная версия')
is_running, lose = True, False
clock = pg.time.Clock()
score = pg.font.SysFont("Verdana", 20)
surf = pg.Surface((390, 390), pg.SRCALPHA)
bg = pg.image.load("background.jpg")
bg = pg.transform.scale(bg, (w, h))
gameover = pg.image.load("game_over.jpg")
gameover = pg.transform.scale(gameover, (390, 390))


class Food:
    def __init__(self):
        self.pic = pg.image.load("cherry.png")
        self.rect = self.pic.get_rect()
        self.spawn_food()

    def spawn_food(self):
        # Задаем рандомные координаты для еды в диапазоне игрового поля с шагом в 40
        self.rect.x = randrange(0, w, step)
        self.rect.y = randrange(0, h, step)

    def draw(self):
        screen.blit(self.pic, self.rect)

    def reset_timer(self):
        self.start_time = time.time()

    def has_expired(self, duration):
        return time.time() - self.start_time >= duration


class Snake:
    def __init__(self):
        self.speed = step
        self.body = [[360, 360]]  # изначальные координаты головы
        self.dx = 0
        self.dy = 0
        self.score = 0
        self.color = 'green'

    def move(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:  # движение змейки по нажатию на клавиатуру
                if event.key == pg.K_a and self.dx == 0:  # чтобы при нажатии налево, змейка не двигалась вправо
                    self.dx = -self.speed
                    self.dy = 0
                if event.key == pg.K_d and self.dx == 0:
                    self.dx = self.speed
                    self.dy = 0
                if event.key == pg.K_w and self.dy == 0:
                    self.dx = 0
                    self.dy = -self.speed
                if event.key == pg.K_s and self.dy == 0:
                    self.dx = 0
                    self.dy = self.speed

        # передвигаем части тела змейки по х и у на предыдущие координаты
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]

        # передвигаем голову змейки по х и у на следующие координаты
        self.body[0][0] += self.dx
        self.body[0][1] += self.dy

        # проверка на столкновение с границами
        if self.body[0][0] < 0 or self.body[0][0] >= w or self.body[0][1] < 0 or self.body[0][1] >= h:
            return True

    def draw(self):
        for part in self.body:
            pg.draw.rect(screen, self.color, (part[0], part[1], step, step))

    # проверяем когда змейка съедает еду
    def collide_food(self, f: Food):
        if self.body[0][0] == f.rect.x and self.body[0][1] == f.rect.y:  # если координаты головы змейки совпадают с координатами еды
            self.score += 1
            self.body.append([1000, 1000])
            f.spawn_food()  # спавн новой еды после съедания

    # заканчиваем игру, если голова змейки столкнеться со своим телом
    def self_collide(self):
        if self.body[0] in self.body[1:]:  # если голова змейки и входит в массив координат тела змейки
            return True


class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.pic = pg.image.load("wall.png")

    def draw(self):
        screen.blit(self.pic, (self.x, self.y))


# создаем объекты змейки и еды
s = Snake()
f = Food()

# задаем таймер для исчезновения еды через 5 секунд
food_timer = 5
f.reset_timer()

# запускаем основной цикл
while is_running:
    clock.tick(fps)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            is_running = False

    screen.blit(bg, (0, 0))

    # вызываем методы классов
    f.draw()
    s.draw()
    collision = s.move(events)  # нажать любую клавишу (a, s, d, w) чтобы начать игру
    s.collide_food(f)
    s.self_collide()

    # проверяем столкновение с границами
    if collision or s.self_collide():
        lose = True

    # считаем время и исчезаемость еды
    if f.has_expired(food_timer):
        f.spawn_food()
        f.reset_timer()

    # высвечиваем текущие баллы и уровень на экран
    counter = score.render(f'Score: {s.score}', True, 'black')
    screen.blit(counter, (50, 50))
    l = score.render(f'Level: {level}', True, 'black')
    screen.blit(l, (50, 80))

    # условие для перехода на следующий уровень
    if s.score == 3:
        level += 1  # увеличиваем уровень
        level %= 4
        fps += 2  # увеличиваем скорость
        s.score = 0  # новый счетчик для следующего уровня

    # запускаем цикл 'game_over'
    while lose:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
                lose = False
        surf.blit(gameover, (0, 0))
        screen.blit(surf, (200, 200))
        cntr = score.render(f'Your score is {s.score}', True, 'white')
        screen.blit(cntr, (320, 405))
        l = score.render(f'Your level is {level}', True, 'white')
        screen.blit(l, (322, 435))
        pg.display.flip()

    pg.display.flip()

pg.quit()
