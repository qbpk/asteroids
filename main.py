#This allows us to use code from the open-source pygame library throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    dt = 0
   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asterfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for inst in updatable:    
            inst.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("GAME OVER!")
                sys.exit()
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()


        #creates pygame Surface object with background color "black"
        screen.fill((0,0,0))

        for inst in drawable:
            inst.draw(screen)

        pygame.display.flip()

        #lock fps to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()