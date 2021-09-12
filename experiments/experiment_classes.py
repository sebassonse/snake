import pygame
#import numpy


class SnakeHead(pygame.sprite.Sprite):
    def __init__(self, x, y, surfhead, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surfhead
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

        # зацикленность игрового поля

        if self.rect.top < 0:
            self.rect.bottom = H
        elif self.rect.bottom > H:
            self.rect.top = 0
        elif self.rect.right > W:
            self.rect.left = 0
        elif self.rect.left < 0:
            self.rect.top = W


class SnakeBody(pygame.sprite.Sprite):
    def __init__(self, surfbody, x, y, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surfbody
        self.rect = self.image.get_rect(topleft=(x, y))
        self.add(group)

    def update(self, cor_pre):
        # moving
        self.rect.x = cor_pre[0]
        self.rect.y = cor_pre[1]





