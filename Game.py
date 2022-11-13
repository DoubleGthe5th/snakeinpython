# Simple pygame program

# Import and initialize the pygame library
import pygame
import time
import random
pygame.init()
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
direction = "down"
def add(tileset,newtile):
    finished = []
    finished.append(newtile)
    for x in range(len(tileset)):
        finished.append(tileset[x])
    return finished
# Run until the user asks to quit
running = True
tiles = [[260,260]]
apple = [100,100]
while running:   	
    for event in pygame.event.get():
        #finds direction
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                if not ([tiles[-1][0],tiles[-1][1] + 20]) in tiles:
                    direction = "down"
            if event.key == K_UP:
                if not ([tiles[-1][0],tiles[-1][1] - 20]) in tiles:
                    direction = "up"
            if event.key == K_LEFT:
                if not ([tiles[-1][0] - 20,tiles[-1][1]]) in tiles:
                    direction = "left"
            if event.key == K_RIGHT:
                if not ([tiles[-1][0] + 20,tiles[-1][1]]) in tiles:
                    direction = "right"
        #quits game
        if event.type == pygame.QUIT:
            running = False
    #makes new squares
    if direction == "up":
        tiles.append([tiles[-1][0],tiles[-1][1] - 20])
    if direction == "down":
        tiles.append([tiles[-1][0],tiles[-1][1] + 20])
    if direction == "left":
        tiles.append([tiles[-1][0] - 20,tiles[-1][1]])
    if direction == "right":
        tiles.append([tiles[-1][0] + 20,tiles[-1][1]])
    tiles.remove(tiles[0])
    #detects apple
    if tiles[-1] == apple:
        if len(tiles) == 1:
            if direction == "up":
                tiles = add(tiles,[tiles[-1][0],tiles[-1][1] - 20])
            if direction == "down":
                tiles = add(tiles,[tiles[-1][0],tiles[-1][1] + 20])
            if direction == "left":
                tiles = add(tiles,[tiles[-1][0] - 20,tiles[-1][1]])
            if direction == "right":
                tiles = add(tiles,[tiles[-1][0] + 20,tiles[-1][1]])
        else:
            if tiles[0][0] - tiles[1][0] == 20:
                tiles = add(tiles,[tiles[0][0] + 20,tiles[0][1]])
            if tiles[0][0] - tiles[1][0] == -20:
                tiles = add(tiles,[tiles[0][0] - 20,tiles[0][1]])
            if tiles[0][1] - tiles[1][1] == -20:
                tiles = add(tiles,[tiles[0][0],tiles[0][1]-20])
            if tiles[0][1] - tiles[1][1] == 20:
                tiles = add(tiles,[tiles[0][0],tiles[0][1]+20])
        #attempts to move apple
        found = False
        while not(found):
            apple = [random.randint(0,24)*20,random.randint(0,24)*20]
            if not(apple in tiles):
                found = True
    #draws squares
    screen.fill((0, 0, 0))
    for tile in tiles:
        print(tile)
        pygame.draw.rect(screen,(0, 255, 0),(tile[0],tile[1],20,20))
    #print apple
    pygame.draw.rect(screen,(255, 0, 0),(apple[0],apple[1],20,20))
    # Flip the display
    pygame.display.flip()
    #detects collision with wall or apple
    if tiles[-1][0] < 0 or tiles[-1][0] >= 500 or  tiles[-1][1] < 0 or tiles[-1][1] >= 500 or (tiles.count(tiles[-1]) >= 2):
        running = False
    time.sleep(.1)
# Done! Time to quit.
pygame.quit()