import pygame
from game import GREEN, BLUE, GREY, WHITE

class Score(pygame.sprite.Sprite):
    output_string = 0
    armor = 0
    
    def __init__(self, width=20, height=25, frame_count = 0):
        super().__init__()
        self.frame_count = frame_count
        self.image = pygame.Surface([width, height])
        self.height = height
        self.width = width
        self.draw()
        self.rect = self.image.get_rect()
        
    def draw(self):
        pygame.draw.rect(self.image, GREY, [0, 0, self.width, 25])
        if(self.frame_count >= 0):           
            self.frame_count += 1 
        output_string = "Armor: " + str(self.armor) + "      Score: {00:04}".format(self.frame_count)
        font = pygame.font.Font(None, 20)
        text = font.render(output_string, True, WHITE)
        self.image.blit(text, [self.width*0.8, 5])
            
    
    def update(self):
        self.draw()
        
    def died(self):
        pygame.mixer.music.load('audio/e-morreu.wav')
        pygame.mixer.music.play() 
        
    def updateItems(self):
        if(self.frame_count >= 0):           
            self.frame_count += 1
            
    def setArmor(self, armor):
        self.armor = armor
        
    def setCount(self, count):
        self.frame_count += count
        