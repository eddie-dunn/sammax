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

        self.rect0 = []
        self.x0 = []
        self.y0 = []

        #~ Used for movement animation

        #~ How many steps to cover distance?
        self.steps_needed = 0

        #~ How many steps have been taken in this animation round?
        self.steps_taken = 0

        #~ How many pixels of movement per step in x and y?
        self.x_comp = 0
        self.y_comp = 0

        #~ sound = pygame.mixer.Sound("geese.mp3")
        #~ sound.play()

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

        for i in range(len(self.boat)):
            self.rect0.append(self.boatpic[i].get_bounding_rect())
            self.x0.append(self.boat[i].drawx - self.rect0[i].width / 2)
            self.y0.append(self.boat[i].drawy - self.rect0[i].width / 2)

        self.run()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
                calc_x = self.boat[0].drawx - self.mouse_x
                calc_y = self.boat[0].drawy - self.mouse_y
                self.degree[0] = math.degrees(math.atan2(calc_x, calc_y))

                #~ Calculate how many steps are needed to cover the distance, and round to nearest integer
                self.steps_needed = round((math.sqrt(calc_x*calc_x + calc_y*calc_y)/self.boat[0].spd), 0)

                print self.steps_needed
                self.x_comp = calc_x/self.steps_needed
                self.y_comp = calc_y/self.steps_needed

                self.steps_taken = 0

                for i in range(len(self.boat)):
                    self.rotatedpic[i] = pygame.transform.rotate(self.boatpic[i], self.degree[i])
                    self.rect0[i] = self.rotatedpic[i].get_bounding_rect()
                    self.x0[i] = self.boat[i].drawx - self.rect0[i].width / 2
                    self.y0[i] = self.boat[i].drawy - self.rect0[i].height / 2

                while self.steps_taken < self.boat[0].spd and self.steps_taken < self.steps_needed:
                    self.steps_taken += 1
                    pygame.time.wait(40)

                    self.boat[0].drawx -= self.x_comp
                    self.boat[0].drawy -= self.y_comp

                    if abs(self.mouse_x-self.boat[0].drawx) <= self.x_comp and abs(self.mouse_y-self.boat[0].drawy) <= self.y_comp:
                        #~ self.boat[0].drawx = self.mouse_x
                        #~ self.boat[0].drawy = self.mouse_y
                        self.steps_taken = self.boat[0].spd

                    self.x0[0] = self.boat[0].drawx - self.rect0[0].width / 2
                    self.y0[0] = self.boat[0].drawy - self.rect0[0].height / 2

                    self.run()

    def run(self):
        self.backg = (0,200,255)
        self.screen.fill(self.backg)

        for i in range(len(self.boat)):
            self.screen.blit(self.rotatedpic[i],(self.x0[i],self.y0[i]))

        pygame.display.flip()
