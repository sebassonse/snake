import pygame
import random
from experiment_classes import SnakeHead
from experiment_classes import SnakeBody

# переменные
Width = 400
Height = 400
FPS = 10
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
surfHead = pygame.Surface((20, 20))
surfHead.fill(GREEN)

surfBody = pygame.Surface((20, 20))
surfBody.fill(BLUE)

surfApple = pygame.Surface((20,20))
surfApple.fill(RED)

# drawing
SH = pygame.sprite.Group()
SB = pygame.sprite.Group()

snake = SnakeHead(Width // 2, Height // 2, surfHead, SH)
snakeBody1 = SnakeBody(surfBody, Width//2, Height//2 + 20, SB)
snakeBody2 = SnakeBody(surfBody, Width//2, Height//2 + 40, SB)

cor_pre = [[Width//2, Height//2 + 20], [Width//2, Height//2 + 40]]


# body cycle
game_over = False
while not game_over:

    # сохраняем события (действия игрока), произошедшие с последнего кадра
    for event in pygame.event.get():
        # закрытие окна нажатием на крестик
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()

    cor_pre.insert(0, [snake.rect.x, snake.rect.y])
    cor_pre.pop(-1)
    for i in range(len(cor_pre)):
        SB.sprites()[i].update(cor_pre[i])
    SH.update(Width, Height, speed, speed_init, keys)
    

    # Отрисовка
    screen.fill(BLACK)
    SH.draw(screen)
    SB.draw(screen)

    # После отрисовки всего, переворачиваем экран
    pygame.display.update()

    # Обновление


    # Держим цикл на нужной нам скорости. Длина кадра = 1/FPS
    clock.tick(FPS)

pygame.quit()
