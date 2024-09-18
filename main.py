#This allows us to use code from the open-source pygame library throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from lives import *

def main():
    pygame.init()
    score = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    ### New feature #1: Scoreboard
    pygame.display.set_caption("Asteroids")
    scoreboardfont = pygame.font.Font('freesansbold.ttf', 24)
    scoreboard = scoreboardfont.render(f"Score: {score}", True, 'green', "black")
    scoreboardrect = scoreboard.get_rect()
    scoreboardrect.center = (SCREEN_WIDTH - SCREEN_WIDTH * .15 , SCREEN_HEIGHT - SCREEN_HEIGHT * .95) 
    ###
    
    dt = 0
   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    
    ### New feature #2: Multiple Lives
    Lives.containers = drawable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asterfield = AsteroidField()

    ### #2: Multiple Lives
    lives = Lives(SCREEN_WIDTH - SCREEN_WIDTH * .18 , SCREEN_HEIGHT - SCREEN_HEIGHT * .90)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for inst in updatable:    
            inst.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player) and player.immunity <= 0:
                player.lives(asteroid.check_collision(player))
                lives.update(player)
                if player.lives_left == 0:
                    print(f"GAME OVER! Final Score: {score}")
                    sys.exit()
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()

                    ### #1: Scoreboard
                    if asteroid.radius == ASTEROID_MAX_RADIUS:
                        score += ASTEROID_MIN_POINTS
                    elif asteroid.radius == ASTEROID_MIN_RADIUS * 2:
                        score += ASTEROID_MID_POINTS
                    else:
                        score += ASTEROID_MAX_POINTS

        #creates pygame Surface object with background color "black"
        screen.fill((0,0,0))

        ### #1: Scoreboard
        scoreboard = scoreboardfont.render(f"Score: {score}", True, 'gold', "black")
        screen.blit(scoreboard, scoreboardrect)

        for inst in drawable:
            inst.draw(screen)

        pygame.display.flip()

        #lock fps to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()