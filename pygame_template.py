import pygame

# переменные
Width = 420
Height = 420
FPS = 2

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# classes and other



# initialisation pygame
pygame.init()

# отображение экрана
Display = pygame.display.set_mode((Width, Height))
# создание заголовка
pygame.display.set_caption('hey')

clock = pygame.time.Clock()

# body cycle
game_over = False
while not game_over:
    # Держим цикл на нужной нам скорости.
    # Длина кадра = 1/FPS
    clock.tick(FPS)
    # сохраняем события (действия игрока), произошедшие с последнего кадрка
    for event in pygame.event.get():
        # закрытие окна нажатием на крестик
        if event.type == pygame.QUIT:
            game_over = True
    # Обновление
    all_sprites.update()
    # Отрисовка
    Display.fill(BLACK)
    
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
