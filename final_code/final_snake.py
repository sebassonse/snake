import pygame
import random

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# переменные
Screen_size = 600
Width = Screen_size
Height = Screen_size
FPS = 10

playing_field_size = 30
snake_size = Screen_size//playing_field_size
apple_size = Screen_size//playing_field_size

snake_speed = Screen_size//playing_field_size
speed = [0, 0]

snakeX_init, snakeY_init = Width//2, Height//2


snake_head = pygame.Surface((snake_size, snake_size))
snake_head.fill(GREEN)
snake_head_rect = snake_head.get_rect(topleft=(snakeX_init, snakeY_init))

snake_placement_list = [tuple([snake_head_rect.x, snake_head_rect.y])]

apple_placement = tuple([snakeX_init, snakeY_init])
# classes and functions


def check_pressed_keys():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and not speed[0] == snake_speed:
        speed[0] = -snake_speed
        speed[1] = 0
        keys = []
    elif keys[pygame.K_RIGHT] and not speed[0] == -snake_speed:
        speed[0] = snake_speed
        speed[1] = 0
        keys = []
    elif keys[pygame.K_UP] and not speed[1] == snake_speed:
        speed[0] = 0
        speed[1] = -snake_speed
        keys = []
    elif keys[pygame.K_DOWN] and not speed[1] == -snake_speed:
        speed[0] = 0
        speed[1] = snake_speed
        keys = []


def walls(snake_head_rect):
    if snake_head_rect.top < 0 or snake_head_rect.bottom > Height\
            or snake_head_rect.right > Width or snake_head_rect.left < 0:
        return True


def apple_generation(Apple_placement, Snake_placement):
    while Apple_placement in Snake_placement:
        appleX = random.randrange(0, Screen_size, apple_size)
        appleY = random.randrange(0, Screen_size, apple_size)
        Apple_placement = tuple([appleX, appleY])
    return Apple_placement


# рисуем яблоко
apple_placement = apple_generation(apple_placement, snake_placement_list)

# initialisation pygame
pygame.init()

# ОФОРМЛЯЛОВО
# отображение экрана
Screen = pygame.display.set_mode((Width, Height))
# отображение заголовка
pygame.display.set_caption('hey, snake')
# а часики-то тикают
clock = pygame.time.Clock()

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

    # ДВИЖЕНИЕ
    # нажатые клавиши
    check_pressed_keys()

    # движение змейки
    snake_head_rect.x += speed[0]
    snake_head_rect.y += speed[1]

    # возводим стены
    game_over_walls = walls(snake_head_rect)
    if game_over_walls:
        break

    # ПОЕДАНИЕ И РОСТ
    # поедание
    if snake_placement_list[0] == apple_placement:
        apple_placement = apple_generation(apple_placement, snake_placement_list)
        snake_placement_list.append(tuple([0, 0]))

    # рост и наследование положения
    snake_placement_list.insert(0, tuple([snake_head_rect.x, snake_head_rect.y]))
    snake_placement_list.pop(-1)

    # ОТРИСОВКА
    Screen.fill(BLACK)
    # Рисуем яблоко
    pygame.draw.rect(Screen, RED, [apple_placement[0] + 2, apple_placement[1] + 2, apple_size-4, apple_size-4])
    # Рисуем змею
    Screen.blit(snake_head, snake_head_rect)
    if len(snake_placement_list) > 1:
        for i in range(len(snake_placement_list)):
            pygame.draw.rect(Screen, GREEN, [snake_placement_list[i][0] + 1, snake_placement_list[i][1] + 1,
                                             snake_size-2, snake_size-2])

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

    # ЕСЛИ ЗМЕЙКА НАТКНУЛАСЬ САМА НА СЕБЯ
    if len(set(snake_placement_list)) < len(snake_placement_list):
        game_over = True

pygame.quit()
