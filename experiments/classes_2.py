import pygame
import random

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# pre-drawing
surfHead = pygame.Surface((20, 20))
surfHead.fill(GREEN)


class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surfHead
        self.rect = self.image.get_rect(topleft=(x, y))
        self.add(group)

    # movement of object
    # speed in format [speedX, speedY]
    # последним передается список keys
    def update(self, W, H, speed, speed_init, *args):
        # змейка инициализируется мордой вверх в середине поля и сразу начинает двигаться
        self.rect.x += speed[0]
        self.rect.y += speed[1]

        # управление направлением движения стрелочками, поворачивать назад нельзя
        for keys in args:
            if keys[pygame.K_LEFT] and not speed[0] == speed_init:
                speed[0] = -speed_init
                speed[1] = 0
            if keys[pygame.K_RIGHT] and not speed[0] == -speed_init:
                speed[0] = speed_init
                speed[1] = 0
            if keys[pygame.K_UP] and not speed[1] == speed_init:
                speed[0] = 0
                speed[1] = -speed_init
            if keys[pygame.K_DOWN] and not speed[1] == -speed_init:
                speed[0] = 0
                speed[1] = speed_init
        # зацикленность игрового поля

        if self.rect.top < 0:
            self.rect.bottom = H
        elif self.rect.bottom > H:
            self.rect.top = 0
        elif self.rect.right > W:
            self.rect.left = 0
        elif self.rect.left < 0:
            self.rect.right = W


class Apple(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = surfApple
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, W, H, apple_placement, snake_placement):
        if apple_placement in snake_placement:
            self.kill()

            appleX_init = random.randrange(0, W, 20)
            appleY_init = random.randrange(0, H, 20)

            if [appleX_init, appleY_init] in snake_placement:
                self.update(W, H, apple_placement, snake_placement)
            else:
                self.__init__(appleX_init, appleY_init)
