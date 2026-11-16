import pygame, sys
pygame.init()

from elements import *
from config import *
import threading

elements = {
    "nodes": [Node("Testing", (50,50), (30,100,40))],
    "lines": [],
    "buttons": [],
    "menus": [],
}

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True
while running:
    
    screen.fill(BACKGROUND_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        for cat in elements:
            for element in elements[cat]:
                element.handle_event(event)
    
    for cat in elements:
        for element in elements[cat]:
            element.draw(screen)
            element.update()
    
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()