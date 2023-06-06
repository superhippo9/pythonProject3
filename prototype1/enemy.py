import pygame, random

class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("/Users/ben/PycharmProjects/pythonProject3/prototype1/graphics/player/enemies-1.png.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 8

    def update(self):
        self.rect.x += random.randint(-5, 5)
        self.rect.y += random.randint(-5, 5)

