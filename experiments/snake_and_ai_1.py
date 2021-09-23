import pygame
import random
import numpy as np

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


def matrix_generation(playing_field_size, snake_size, snake_placement_list, apple_placement):
    M = np.ones((playing_field_size, playing_field_size))
    for i in range(1, len(snake_placement_list)):
        s_p_l_array = np.floor_divide(snake_placement_list[i], snake_size)
        M[s_p_l_array[1], s_p_l_array[0]] = 5

    s_h_p_array = np.floor_divide(snake_placement_list[0], snake_size)
    M[s_h_p_array[1], s_h_p_array[0]] = 6
    a_p_array = np.floor_divide(apple_placement, snake_size)
    M[a_p_array[1], a_p_array[0]] = 10


def closest_barrier(snake_placement_list, snake_head_rect, screen_size, snake_size):
    snake_placement_list_X = []
    snake_placement_list_Y = []
    onTheWayVert = []
    onTheWayHoriz = []
    barriersDown = []
    barriersUp = []
    barriersRight = []
    barriersLeft = []
    for i in range(len(snake_placement_list)):
        snake_placement_list_X.append(snake_placement_list[i][0])
        snake_placement_list_Y.append(snake_placement_list[i][1])

    for i in range(len(snake_placement_list)):
        if snake_head_rect.x == snake_placement_list_X[i]:
            onTheWayVert.append(int(i))
        if snake_head_rect.y == snake_placement_list_Y[i]:
            onTheWayHoriz.append(int(i))

    if len(onTheWayVert) > 0:
        # distance y
        for j in range(len(onTheWayVert)):
            if snake_head_rect.y - snake_placement_list[onTheWayVert[j]][1] < 0:
                barriersDown.append(abs(snake_head_rect.bottom - snake_placement_list[onTheWayVert[j]][1]))
            if snake_head_rect.y - snake_placement_list[onTheWayVert[j]][1] > 0:
                barriersUp.append(abs(snake_head_rect.top - (snake_placement_list[onTheWayVert[j]][1] + snake_size)))

    if len(barriersUp) == 0:
        barriersUp.append(abs(snake_head_rect.top))
    if len(barriersDown) == 0:
        barriersDown.append(abs(snake_head_rect.bottom - screen_size))

    if len(onTheWayHoriz) > 0:
        # distance x
        for j in range(len(onTheWayHoriz)):
            if snake_head_rect.x - snake_placement_list[onTheWayHoriz[j]][0] < 0:
                barriersRight.append(abs(snake_head_rect.right - snake_placement_list[onTheWayHoriz[j]][0]))
            if snake_head_rect.x - snake_placement_list[onTheWayHoriz[j]][0] > 0:
                barriersLeft.append(abs(snake_head_rect.left - (snake_placement_list[onTheWayHoriz[j]][0] + snake_size)))

    if len(barriersLeft) == 0:
        barriersLeft.append(abs(snake_head_rect.left))
    if len(barriersRight) == 0:
        barriersRight.append(abs(snake_head_rect.right - screen_size))

    return [min(barriersUp), min(barriersRight), min(barriersDown), min(barriersLeft)]


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

    # ПОЕДАНИЕ И РОСТ
    # поедание
    if snake_placement_list[0] == apple_placement:
        apple_placement = apple_generation(apple_placement, snake_placement_list)
        snake_placement_list.append(tuple([0, 0]))

    # рост и наследование положения
    snake_placement_list.insert(0, tuple([snake_head_rect.x, snake_head_rect.y]))
    snake_placement_list.pop(-1)

    # возводим стены
    game_over_walls = walls(snake_head_rect)
    if game_over_walls:
        break

    # ЕСЛИ ЗМЕЙКА НАТКНУЛАСЬ САМА НА СЕБЯ
    if len(set(snake_placement_list)) < len(snake_placement_list):
        break

    # matrix generation
    matrix_generation(playing_field_size, snake_size, snake_placement_list, apple_placement)

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

    # FEATURES

    # distance to the walls and snake body
    closestBarriers = closest_barrier(snake_placement_list, snake_head_rect, Screen_size, snake_size)
    print(closestBarriers)

pygame.quit()
