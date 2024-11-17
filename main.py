# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shots import Bullet

def main():
    pygame.init() #Initialize all imported pygame modules
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Bullet.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over")
                return
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.split()
            
        screen.fill("black") #Fills the screen surface with a color

        for object in drawable:
            object.draw(screen)    

        pygame.display.flip() #Refreshes the screen
        dt = clock.tick(60) / 1000 #Limit the frametime to 60 FPS
        
        
if __name__ == "__main__":
    main()
