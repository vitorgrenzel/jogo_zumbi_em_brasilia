import pygame

BLACK = (0, 0, 0)
GREEN = (84, 171, 71)
GREY = (50, 50, 50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

class Game:
    def __init__(self, title='Game', width=800, height=600, tick=30, running=True):
        self.width = width
        self.height = height
        self.tick = tick
        self.running = running

        self.allSprites = pygame.sprite.Group()
        
        pygame.init()
        self.display = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.loop()
    
    def __del__(self):
        pygame.quit()
    
    def handleEvent(self, event):
        pass

    def buildItems(self):
        pass

    def updateItems(self):
        pass
    
    def menu(self):
        self.display.fill(RED)
        font = pygame.font.Font(None, 50)
        text = font.render("Apocalipse 2018", True, WHITE)
        self.display.blit(text, [self.width*0.6, self.height*0.5])
        pygame.mixer.music.load('audio/to-be-continue.wav')
        pygame.mixer.music.play()
        pygame.display.update()
        self.clock.tick(self.tick)

    def loop(self):
        self.clock = pygame.time.Clock()
        self.menu()
        pygame.time.delay(5000)
        self.buildItems()

        while self.running:
            self.handleEvent()
            self.updateItems()
            self.allSprites.update()
            self.allSprites.draw(self.display)

            pygame.display.update() 
            self.clock.tick(self.tick)
