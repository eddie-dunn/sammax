import os, sys, pygame, random, math
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class BoatGfx():

    def __init__(self, boat, width = 800, height = 800):
        pygame.init()

        self.boat = boat
        self.boatpic = pygame.image.load(boat._picpath)

        self.rotatedpic = self.boatpic
        self.degree = []
        self.rotate = 0

        self.rect0 = []
        self.x0 = []
        self.y0 = []

        self.width = width
        self.height = height
        self.size = self.width, self.height
        self.backg = 0,0,0

        self.screen = pygame.display.set_mode(self.size)

        self.mouse_x = 1
        self.mouse_y = 1

        self.degree.append(0)


        self.rect0 = self.boatpic.get_bounding_rect()
        self.x0 = (self.boat.location[0] - self.rect0.width / 2)
        self.y0 = (self.boat.location[1] - self.rect0.width / 2)

        self.drawToBuffer()
        self.drawToScreen()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.boat.set_destination(pygame.mouse.get_pos())

    def drawToBuffer(self):
        self.backg = (0,200,255)
        self.screen.fill(self.backg)

        self.rotatedpic = pygame.transform.rotate(self.boatpic, self.boat.heading +180)
        self.rect0 = self.rotatedpic.get_bounding_rect()
        self.x0 = self.rect0.width / 2
        self.y0 = self.rect0.height / 2

        self.screen.blit(self.rotatedpic,(self.boat.location[0]-self.x0,self.boat.location[1]-self.y0))


    def drawToScreen(self):
        pygame.display.flip()
