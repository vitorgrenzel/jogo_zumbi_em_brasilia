import pygame

from game import WHITE, BLACK
from bullet import Bullet


class Character(pygame.sprite.Sprite):
    i = 0
    timer = 0
    opponent_type = 0
    
    player_images = []
    player_images.append( pygame.image.load("imgs\player-frame-0.png") )
    player_images.append( pygame.image.load("imgs\player-frame-1.png") )
    
    oponnent_images = []
    oponnent_images.append( pygame.image.load("imgs\zumbi1-frame-0.png") )
    oponnent_images.append( pygame.image.load("imgs\zumbi2-frame-0.png") )
    oponnent_images.append( pygame.image.load("imgs\zumbi3-frame-0.png") )
    oponnent_images.append( pygame.image.load("imgs\zumbi1-frame-1.png") )
    oponnent_images.append( pygame.image.load("imgs\zumbi2-frame-1.png") )
    oponnent_images.append( pygame.image.load("imgs\zumbi3-frame-1.png") )
    oponnent_images.append( pygame.image.load("imgs\zumbi3-frame-1.png") )
    
    def __init__(self, character, width, height, player=False, speed = 5):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.player = player
        self.height = height
        self.width = width
        self.character = character
        self.opponent_type = character
        self.speed = speed
        self.draw()
        self.rect = self.image.get_rect()
    
    def draw(self):
        if not self.player:
            if(self.timer%3 == 0):
                self.image = self.oponnent_images[ self.character ]
                if(self.opponent_type == self.character):
                    self.character += 3
                else:
                    self.character -= 3
            self.timer += 1
        else:
            if(self.timer%3 == 0):
                self.image = self.player_images[ self.i ]
            self.timer += 1
            if(self.i == 1):
                self.i = 0
            else:
                self.i += 1 
    
    def update(self):
        self.draw()
        if not self.player:
            self.moveLeft(self.speed)

    def moveRight(self, pixels):
        self.rect.move_ip(pixels, 0)
 
    def moveLeft(self, pixels):
        self.rect.move_ip(-pixels, 0)
    
    def moveTop(self, pixels):
        self.rect.move_ip(0, -pixels)
 
    def moveBottom(self, pixels):
        self.rect.move_ip(0, pixels)
    
    def changeSpeed(self, speed):
        self.speed = speed
        
    def shoot(self):
        pygame.mixer.music.load('audio/tiro.wav')
        pygame.mixer.music.play()
        bullet = Bullet(self.moveSpeed*3)
        bullet.rect.x = self.player.rect.x + (self.carWidth)
        bullet.rect.y = self.player.rect.y + (self.carHeight*0.3)
        self.allSprites.add(bullet)
        self.bullets.add(bullet)
