import os, sys, pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class BoatGfx():

    def __init__(self, boat, width = 600, height = 400):
        pygame.init()

        self.boat = boat
        self.boatpic = []

        sound = pygame.mixer.Sound("geese.mp3")
        sound.play()

        self.size = width, height
        self.backg = 0,0,0

        self.screen = pygame.display.set_mode(self.size)

        for item in self.boat:
            self.boatpic.append(pygame.image.load(item.picpath))

        self.x1 = [1, 1]
        self.y1 = [1, 1]

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        self.backg = self.boat[0].drawx%255, self.boat[0].drawy%255, ((self.boat[0].drawx+self.boat[0].drawy)%255)
        self.screen.fill(self.backg)

        for i in range(len(self.boat)):
            self.screen.blit(self.boatpic[i],(self.boat[i].drawx,self.boat[i].drawy))

        pygame.display.flip()

        for i in range(len(self.boat)):
            if self.boat[i].drawx == self.width:
                self.x1[i] = -1
            elif self.boat[i].drawx == 0:
                self.x1[i] = 1
            if self.boat[i].drawy == self.height:
                self.y1[i] = -1
            elif self.boat[i].drawy == 0:
                self.y1[i] = 1

        for i in range(len(self.boat)):
            self.boat[i].drawx = self.boat[i].drawx+self.x1[i]
            self.boat[i].drawy = self.boat[i].drawy+self.y1[i]
