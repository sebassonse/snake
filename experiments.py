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


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (Width/2, Height/2)

    def update(self):
        self.rect.y -= 20
        if self.rect.top < 0:
            self.rect.bottom = Height

# initialisation pygame
pygame.init()

# отображение экрана
Display = pygame.display.set_mode((Width, Height))
# создание заголовка
pygame.display.set_caption('snake')

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
snake = Snake()
all_sprites.add(snake)

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
    all_sprites.draw(Display)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()

