import pygame
import numpy


class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(topleft=(x, y))
        self.add(group)
        # self.speed = speed

    # movement of object
    # speed in format [speedX, speedY]
    # последним передается список keys
    def update(self, W, H, speed, speed_init, n, *args):
        # змейка инициализируется мордой вверх в середине поля и сразу начинает двигаться
        if n == 10:
            self.rect.x += speed[0]
            self.rect.y += speed[1]
        for Key in args:
            if Key[pygame.K_LEFT] and not speed[0] == speed_init:
                speed[0] = -speed_init
                speed[1] = 0
            if Key[pygame.K_RIGHT] and not speed[0] == -speed_init:
                speed[0] = speed_init
                speed[1] = 0
            if Key[pygame.K_UP] and not speed[1] == speed_init:
                speed[0] = 0
                speed[1] = -speed_init
            if Key[pygame.K_DOWN] and not speed[1] == -speed_init:
                speed[0] = 0
                speed[1] = speed_init

        if self.rect.top < 0:
            self.rect.bottom = H
        elif self.rect.bottom > H:
            self.rect.top = 0
        elif self.rect.right > W:
            self.rect.left = 0
        elif self.rect.left < 0:
            self.rect.top = W

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, surf):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf


