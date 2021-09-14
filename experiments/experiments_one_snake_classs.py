import pygame
import random
from classes_2 import Snake

# переменные
Width = 600
Height = 600
FPS = 10

snake_size = 20
apple_size = snake_size
speed_init = snake_size
speed = [0, -speed_init]

appleX_init = random.randrange(0, Width, apple_size)
appleY_init = random.randrange(0, Height, apple_size)

snake_placement = [[Width // 2, Height // 2]]
# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# pre-drawing
surfApple = pygame.Surface((20, 20))
surfApple.fill(RED)

# classes and functions


# initialisation pygame
pygame.init()


# отображение экрана
screen = pygame.display.set_mode((Width, Height))
# отображение заголовка
pygame.display.set_caption('hey')
# а часики-то тикают
clock = pygame.time.Clock()

#
SG = pygame.sprite.Group()
snake = Snake(Width // 2, Height // 2, SG)
snake_list_len = 1

# body cycle
game_over = False
while not game_over:

    # Держим цикл на нужной нам скорости. Длина кадра = 1/FPS
    clock.tick(FPS)

    # сохраняем события (действия игрока), произошедшие с последнего кадра
    for event in pygame.event.get():
        # закрытие окна нажатием на крестик
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()

    if snake_list_len > 1:
        for i in range(1, snake_list_len-1):
            snake_placement[-i] = snake_placement[-i-1]

    snake_placement[0] = [snake.rect.x, snake.rect.y]
    # apple
    while [appleX_init, appleY_init] in snake_placement:
        appleX_init = random.randrange(0, Width, snake_size)
        appleY_init = random.randrange(0, Height, snake_size)

    # Обновление головы
    SG.update(Width, Height, speed, speed_init, keys)

    if [appleX_init, appleY_init] in snake_placement:
        snake_list_len += 1
        snake_placement.append([0, 0])
    # Отрисовка
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, [appleX_init, appleY_init, apple_size, apple_size])
    SG.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
