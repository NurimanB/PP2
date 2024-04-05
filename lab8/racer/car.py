import pygame as pg
import random, time
pg.init()

w, h, fps = 400, 600, 60
is_running, lose = True, False
screen = pg.display.set_mode((w, h))
pg.display.set_caption('racer')
clock = pg.time.Clock()
y = 0
ry = 2
step, enemy_step, score, score_coin = 5, 5, 0, 0
game_over = pg.image.load("gameover.jpg")
bg = pg.image.load("track.png")
game_over = pg.transform.scale(game_over, (w, h))
# задаем фонт для текста
score_font = pg.font.SysFont("Verdana", 20)
score_coins = pg.font.SysFont("Verdana", 20)

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Enemy.jng") # загружаем картинку
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), 0) # задаем рандомные координаты

    def update(self):
        global score
        self.rect.move_ip(0, enemy_step) # движение этой машинки по оси у сверху вниз
        if(self.rect.bottom > h + 90): 
            score += 1 # добавляем 1 когда эта машинка проедет вниз и не столкнеться с игровой машинкой
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface): # отрисовываем машинку
        surface.blit(self.image, self.rect)


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Player.png") # загружаем картинку
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self): # движение игровой машинки по х и у с помощью клавиш
        pressed_keys = pg.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pg.K_a]:
                self.rect.move_ip(-step, 0)

        if self.rect.right < w:
            if pressed_keys[pg.K_d]:
                self.rect.move_ip(step, 0)

        if self.rect.top > 0:
            if pressed_keys[pg.K_w]:
                self.rect.move_ip(0, -step)
            
        if self.rect.bottom < h:
            if pressed_keys[pg.K_s]:
                self.rect.move_ip(0, step)        

    def draw(self, surface): # отрисовываем машинку
        surface.blit(self.image, self.rect)

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("coin.png") # загружаем картинку
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, w - 30), random.randint(30, h - 130)) # рандомные координаты для монетки

    def draw(self): # отрисовываем монетку
        screen.blit(self.image, self.rect)
# создаем объекты
p = Player()
e = Enemy()
c = Coin()
# создаем группы и добавляем туда объекты
enemies = pg.sprite.Group()
enemies.add(e)

coins = pg.sprite.Group()
coins.add(c)

# запускаем основной цикл
while is_running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
    # анимируем движущийся фон
    screen.blit(pg.transform.scale(bg, (w, h)), (0, y % h))
    screen.blit(pg.transform.scale(bg, (w, h)), (0, -h + (y % h)))
    y += ry

    p.update()
    e.update()
    # условие для столкновения игровой машинки с "энеми" машинкой
    if pg.sprite.spritecollideany(p, enemies):
        lose = True # запускаем цикл "game over"

    for c in coins:
        c.draw()
        if pg.sprite.collide_rect(p, c): # если игровая машинка получит монетку
            c.kill() 
            score_coin += 1
            new = Coin() # заново создаем объект монетки
            coins.add(new) # добавляем новый объект в массив монеток

    e.draw(screen)
    p.draw(screen)

    # цикл "game over"
    while lose:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        screen.blit(game_over, (0, 0))
        pg.display.flip()
    # высвечиваем скор в правом верхнем углу
    counter = score_coins.render(f'Coins: {score_coin}', True, 'white')
    screen.blit(counter, (300, 10))
    
    pg.display.flip()
pg.quit()