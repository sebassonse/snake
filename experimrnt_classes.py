import pygame


class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.add(group)
    # movement of object
    def update(self, speed):
        if event.type == pygame.KEYDOWN:
