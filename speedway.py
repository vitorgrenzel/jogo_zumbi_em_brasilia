import pygame

from game import GREEN, BLUE, GREY

class Speedway(pygame.sprite.Sprite):
    i = 0
    timer = 0
    position = True
    background_images = []
    background_images.append( pygame.image.load("imgs/background-frame-0.jpg") )
    background_images.append( pygame.image.load("imgs/background-frame-1.jpg") )
    background_images.append( pygame.image.load("imgs/background-frame-2.jpg") )
    background_images.append( pygame.image.load("imgs/background-frame-3.jpg") )
    
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.draw()
        self.rect = self.image.get_rect()
        
    def draw(self):
        if(self.timer%5 == 0):
            self.image = self.background_images[ self.i ]
        self.timer += 1    
        if(self.i == 1):
            self.i = 0
        else:
            self.i += 1
        
    def update(self):
        self.draw()
