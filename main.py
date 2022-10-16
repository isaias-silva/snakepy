#libs

import pygame
from pygame.locals import *

from util import colid, randomGrid

#iniciando
pygame.init()
#direções constantes
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4
#direcao inicial
mydir = LEFT


screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("cobrinha")

snake = [(200, 200), (210, 200), (220, 200)]


snakeSkin = pygame.Surface((10, 10))
snakeSkin.fill((255, 255, 0))

apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))
applePosition = randomGrid()


clock = pygame.time.Clock()


while True:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:

            if event.key == K_UP:
                if (mydir != DOWN):
                    mydir = UP
            if event.key == K_DOWN:
                if (mydir != UP):
                    mydir = DOWN
            if event.key == K_LEFT:
                if (mydir != RIGHT):
                    mydir = LEFT
            if event.key == K_RIGHT:
                if (mydir != LEFT):
                    mydir = RIGHT

    if mydir == UP:
        snake[0] = (snake[0][0], snake[0][1]-10)
    if mydir == DOWN:
        snake[0] = (snake[0][0], snake[0][1]+10)
    if mydir == RIGHT:
        snake[0] = (snake[0][0]+10, snake[0][1])
    if mydir == LEFT:
        snake[0] = (snake[0][0]-10, snake[0][1])
    for i in range(len(snake)-1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
    screen.fill((0, 0, 0))
    if (colid(snake[0], applePosition) == True):
        snake.append((snake[-1][0]+10, snake[-1][1]))
        applePosition = randomGrid()

    if (colid(snake[0], (0, snake[0][1])) == True):
        snake[0] = (580, snake[0][1])
     
    if (colid(snake[0], (600, snake[0][1])) == True):
        snake[0] = (10, snake[0][1])
     
    if (colid(snake[0], (snake[0][0],0)) == True):
        snake[0] = (snake[0][0],380)
      
    if (colid(snake[0], (snake[0][0],400)) == True):
        snake[0] = (snake[0][0],10)
    

    for pos in snake:
        screen.blit(snakeSkin, pos)
        screen.blit(apple, applePosition)
    pygame.display.update()
