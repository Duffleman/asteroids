# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init() #Initialize all imported pygame modules
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt) #This calls the update function to move the player before each screen is drawn
            
        screen.fill("black") #Fills the screen surface with a color
        player.draw(screen)
        pygame.display.flip() #Refreshes the screen
        
        dt = clock.tick(60) / 1000 #Limit the frametime to 60 FPS
        
        
if __name__ == "__main__":
    main()
