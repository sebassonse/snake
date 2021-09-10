import pygame
from experiment_classes import Snake

# переменные
Width = 400
Height = 400
FPS = 20
n = 0

X_sn_init, Y_sn_init = Width/2, Height/2
speed_init = 20
speed = [0, -speed_init]

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# classes and other


# initialisation pygame
pygame.init()

# оформлялово

# отображение экрана
screen = pygame.display.set_mode((Width, Height))
# отображение заголовка
pygame.display.set_caption('hey')
# а часики-то тикают
clock = pygame.time.Clock()


# pre-drawing
surf = pygame.Surface((20, 20))
surf.fill(GREEN)
# drawing
SG = pygame.sprite.Group()
snake = Snake(Width//2, Height//2, surf, SG)


# body cycle
game_over = False
while not game_over:

    # сохраняем события (действия игрока), произошедшие с последнего кадра
    for event in pygame.event.get():
        # закрытие окна нажатием на крестик
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if n < 10:
        n += 1
    else:
        n = 0
    SG.update(Width, Height, speed, speed_init, n, keys)
    # Отрисовка
    screen.fill(BLACK)
    SG.draw(screen)

    # После отрисовки всего, переворачиваем экран
    pygame.display.update()

    # Обновление


    # Держим цикл на нужной нам скорости. Длина кадра = 1/FPS
    clock.tick(FPS)

pygame.quit()
