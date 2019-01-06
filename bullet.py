import pygame
from game import BLACK

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, speed = 5, color = BLACK, width=20, height=10):
        super().__init__()
        self.height = height
        self.width = width
        self.color = color
        self.speed = speed
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.draw()
        self.rect = self.image.get_rect()
     
    def draw(self):
        self.image = pygame.image.load("imgs/bullet.png")
            
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 1024:
            self.kill()