import pygame
import sys
from node import Node


pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (30, 40, 50)


test = Node("Testingasdfghjkl;'werghbfdertghfdr5678ikmnbvcx[m,kuytf]", (50,50), (100, 110, 130), [4, 5])

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

running = True
while running:
    
    screen.fill(BG_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    test.draw(screen)
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()