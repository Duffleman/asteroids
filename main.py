# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init() #Initialize all imported pygame modules
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    keep_going = True
    while keep_going:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0)) #Fills the screen surface with a color
        pygame.display.flip() #Refreshes the screen
 
if __name__ == "__main__":
    main()
