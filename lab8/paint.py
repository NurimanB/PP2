import pygame  
pygame.init()  

fps = 5000  # установка фпс
timer = pygame.time.Clock()  # создание объекта Clock для управления фпс
WIDTH, HEIGHT = 800, 600  # размеры экрана
active_size = 0  # изначальный размер активного инструмента
active_color = 'white'  # изначальный цвет активного инструмента
painting = []  # список для хранения рисунка
current_tool = 'brush'  # изначально выбранный инструмент - кисть

screen = pygame.display.set_mode([WIDTH, HEIGHT])  # создание окна отображения с заданными размерами
pygame.display.set_caption("paint")  # название окна

# функция для отрисовки меню с выбором цвета и размера кисти
def draw_menu(color, size):
    # отрисовка верхней панели меню
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70))
    
    # отрисовка кнопок для выбора размера кисти
    xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    l_brush = pygame.draw.rect(screen, 'black', [70, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (95, 35), 15)
    m_brush = pygame.draw.rect(screen, 'black', [130, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (155, 35), 10)
    s_brush = pygame.draw.rect(screen, 'black', [190, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (215, 35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]  # список кнопок для выбора размера кисти
    
    # отрисовка кнопок для выбора цвета
    pygame.draw.circle(screen, color, (400, 35), 30)
    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    white = pygame.draw.rect(screen, (255, 255, 255), [WIDTH - 110, 10, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 35, 25, 25])
    circle_button = pygame.draw.rect(screen, 'black', [250, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (275, 35), 20)
    rectangle_button = pygame.draw.rect(screen, 'black', [310, 10, 50, 50])
    pygame.draw.rect(screen, 'white', [315, 15, 40, 40])
    color_rect = [blue, red, green, yellow, teal, purple, white, black, circle_button, rectangle_button]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 255, 255), (0, 0, 0), None, None]
    
    return brush_list, color_rect, rgb_list  # возвращение списков кнопок и соответствующих значений цветов

# функция для отрисовки рисунка
def draw_painting(paints):
    for i in range(len(paints)):
        if paints[i][0] == 'circle':  # если рисуем круг
            pygame.draw.circle(screen, paints[i][1], paints[i][2], paints[i][3])  # отрисовка круга
        elif paints[i][0] == 'rectangle':  # если рисуем прямоугольник
            pygame.draw.rect(screen, paints[i][1], paints[i][2])  # отрисовка прямоугольника
        else:  # если рисуем кистью
            pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])  # отрисовка круга

# основной игровой цикл
running = True
while running:
    timer.tick(fps)  # управление фпс
    
    screen.fill("white")  # заполнение экрана белым цветом
    mouse = pygame.mouse.get_pos()  # получение текущей позиции мыши
    left_click = pygame.mouse.get_pressed()[0]  # получение состояния левой кнопки мыши
    
    # если нажата левая кнопка мыши и мышь находится в пределах области для рисования (ниже панели меню)
    if left_click and mouse[1] > 70:
        if current_tool == 'brush':  # если выбран инструмент "кисть"
            painting.append((active_color, mouse, active_size))  # добавление точки в список рисунка
        elif current_tool == 'circle':  # если выбран инструмент "круг"
            painting.append(('circle', active_color, mouse, active_size*3))  # добавление круга в список рисунка
        elif current_tool == 'rectangle':  # если выбран инструмент "прямоугольник"
            rect_width = 4 * active_size
            rect_height = 4 * active_size
            rect_x = mouse[0] - active_size
            rect_y = mouse[1] - active_size
            painting.append(('rectangle', active_color, pygame.Rect(rect_x, rect_y, rect_width, rect_height)))  # добавление прямоугольника в список рисунка
    
    draw_painting(painting)  # отрисовка рисунка
    
    # отрисовка курсора кисти, если выбран инструмент "кисть"
    if mouse[1] > 70 and current_tool == 'brush':
        pygame.draw.circle(screen, active_color, mouse, active_size)
        
    # отрисовка меню и получение списка кнопок и соответствующих значений цветов
    brushes, colors, rgbs = draw_menu(active_color, active_size)

    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # если событие - выход из программы
            running = False  # завершение игрового цикла
            
        if event.type == pygame.MOUSEBUTTONDOWN:  # если нажата кнопка мыши
            for i in range(len(brushes)):  # проверка каждой кнопки изменения размера кисти
                if brushes[i].collidepoint(event.pos):  # если нажата кнопка изменения размера кисти
                    active_size = 20 - (i * 5)  # изменение размера кисти в зависимости от выбранной кнопки

            for i in range(len(colors)):  # проверка каждой кнопки выбора цвета
                if colors[i].collidepoint(event.pos):  # если нажата кнопка выбора цвета
                    if rgbs[i] is not None:  # если выбран цвет из заданного набора
                        active_color = rgbs[i]  # установка активного цвета
                    else:  # если выбран инструмент
                        if i == len(colors) - 2:  # если выбран инструмент "круг"
                            current_tool = 'circle'  # установка текущего инструмента "круг"
                        elif i == len(colors) - 1:  # если выбран инструмент "прямоугольник"
                            current_tool = 'rectangle'  # установка текущего инструмента "прямоугольник"
    
    pygame.display.flip()  # обновление экрана

pygame.quit()  # выход из pygame