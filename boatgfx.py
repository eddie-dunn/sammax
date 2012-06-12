import os, sys, pygame, random, math
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class BoatGfx():

    def __init__(self, boat, width = 600, height = 400):
        pygame.init()

        self.boat = boat
        self.boatpic = []

        self.rotatedpic = []
        self.degree = []
        self.rotate = 0

        sound = pygame.mixer.Sound("geese.mp3")
        sound.play()

        self.width = width
        self.height = height
        self.size = self.width, self.height
        self.backg = 0,0,0

        self.screen = pygame.display.set_mode(self.size)

        self.mouse_x = 1
        self.mouse_y = 1

        for item in self.boat:
            self.boatpic.append(pygame.image.load(item.picpath))
            self.rotatedpic.append(pygame.image.load(item.picpath))

            self.degree.append(0)

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == MOUSEMOTION:
                self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
                calc_x = self.boat[0].drawx - self.mouse_x
                calc_y = self.boat[0].drawy - self.mouse_y
                self.degree[0] = math.degrees(math.atan2(calc_x, calc_y))

                self.boat[0].drawx = self.mouse_x;
                self.boat[0].drawy = self.mouse_y;
                
                #self.boat[0].targetheadingx = self.mouse_x
                #self.boat[0].targetheadingy = self.mouse_y

    def run(self):
        self.backg = (0,200,255)
        self.screen.fill(self.backg)

        for i in range(len(self.boat)):
            #self.degree[i] = math.degrees(math.atan2(self.boat[i].ix, self.boat[i].iy))
            self.rotatedpic[i] = pygame.transform.rotate(self.boatpic[i], self.degree[i])
            rect0 = self.rotatedpic[i].get_bounding_rect()
            x0 = self.boat[i].drawx - rect0.width / 2 
            y0 = self.boat[i].drawy - rect0.height / 2 
            #self.screen.blit(self.rotatedpic[i],(self.boat[i].drawx,self.boat[i].drawy))
            self.screen.blit(self.rotatedpic[i],(x0,y0))


        pygame.display.flip()

        #~ for i in range(len(self.boat)):
            #~ if self.boat[i].drawx >= self.width:
                #~ self.x1[i] = -1
            #~ elif self.boat[i].drawx <= 0:
                #~ self.x1[i] = 1
            #~ if self.boat[i].drawy >= self.height:
                #~ self.y1[i] = -1
            #~ elif self.boat[i].drawy <= 0:
                #~ self.y1[i] = 1

        #~ for i in range(len(self.boat)):
            #~ self.boat[i].drawx = self.boat[i].drawx+(self.x1[i]*random.randint(1, 3))
            #~ self.boat[i].drawy = self.boat[i].drawy+(self.y1[i]*random.randint(1, 3))
            #~ self.degree[i] += random.randint(0, 3)
