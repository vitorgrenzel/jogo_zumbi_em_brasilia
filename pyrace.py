import pygame

from game import Game, CYAN, GREY, RED, BLUE, BLACK, WHITE
from character import Character
from bullet import Bullet
from speedway import Speedway
from score import Score
from random import randint

class PyRace(Game):
    carWidth = 100
    carHeight = 150
    moveSpeed = 4
    weapon = 4
    
    def buildItems(self):
        speedway = Speedway(self.width, self.height)
        self.allSprites.add(speedway)
        self.score = Score(self.width)
        self.allSprites.add(self.score)
        self.positions = [ (self.height/1.02)-self.carHeight, (self.height/1.02)-self.carHeight*2, (self.height/1.02)-self.carHeight*1.5, (self.height/1.02)-self.carHeight*1.8, (self.height/1.02)-self.carHeight*0.8,]

        player = Character(1, self.carWidth, self.carHeight, True)
        player.rect.x = 25
        player.rect.y = (self.height/1.02) - self.carHeight
        self.allSprites.add(player)
        self.player = player

        self.opponents = pygame.sprite.Group()

        opponentRed = Character(randint(0,2), self.carWidth, self.carHeight, False)
        opponentRed.rect.x = self.width-1
        opponentRed.rect.y = self.positions[0]
        self.allSprites.add(opponentRed)
        self.opponents.add(opponentRed)

        opponentBlue = Character(randint(0,2), self.carWidth, self.carHeight, False)
        opponentBlue.rect.x = self.width-self.carWidth
        opponentBlue.rect.y = self.positions[1]
        self.allSprites.add(opponentBlue)
        self.opponents.add(opponentBlue)
        
        self.bullets = pygame.sprite.Group()

    def handleEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if(self.weapon > 0 ):
                        Character.shoot(self)
                        self.weapon -= 1
                        self.score.setArmor(self.weapon)
                        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if(self.player.rect.x > 0):
                self.player.moveLeft(self.moveSpeed)
        if keys[pygame.K_RIGHT]:
            self.player.moveRight(self.moveSpeed)
        if keys[pygame.K_UP]:
            if(self.player.rect.y > self.height*0.5):
                self.player.moveTop(self.moveSpeed)
        if keys[pygame.K_DOWN]:
            if(self.player.rect.y + self.carHeight < self.height):
                self.player.moveBottom(self.moveSpeed)

        if pygame.sprite.spritecollide(self.player, self.opponents, False):
            print("You died!")
            self.score.died()
            pygame.time.delay(1000)
            self.running = False

        for opponent in self.opponents:
            hits = pygame.sprite.groupcollide(self.opponents, self.bullets, True, True)
            if not opponent.rect.colliderect(self.display.get_rect()) and opponent.rect.x < 0:
                self.moveSpeed += 1
                opponent.kill()
                newOpponent = Character(randint(0,2), self.carWidth, self.carHeight, False, self.moveSpeed)
                newOpponent.rect.x = self.width
                newOpponent.rect.y = self.positions[randint(0,4)]
                self.allSprites.add(newOpponent)
                self.opponents.add(newOpponent)
                opponent.changeSpeed(self.moveSpeed)
                
            for hit in hits:
                hit.kill()
                self.weapon += 1
                self.score.setArmor(self.weapon)
                self.score.setCount(200)
                self.moveSpeed += 1
                newOpponent = Character(randint(0,2), self.carWidth, self.carHeight, False, self.moveSpeed)
                newOpponent.rect.x = self.width
                newOpponent.rect.y = self.positions[randint(0,4)]
                self.allSprites.add(newOpponent)
                self.opponents.add(newOpponent)
                opponent.changeSpeed(self.moveSpeed)

PyRace('PyRace', 1024, 576)
