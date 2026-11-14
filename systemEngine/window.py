import pygame
import sys
from node import Node

# To-Do List:
# TODO: standardize all camelcase and snakecase to only snake case for convention's sake
# TODO: write function/class descriptors
# TODO: improve readability and understandability of comments

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (30, 40, 50)


test = Node("Testingasdfghjkl;'werghbfdertghfdr5678ikmnbvcx[m,kuytf]", (50,50), (100, 110, 130), [7, 3])

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
node_editor = pygame.Surface((800, 600))  # scrollable surface on to which all the nodes and lines are drawn
clock = pygame.time.Clock()

running = True
while running:
    
    node_editor.fill(BG_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        test.handleEvent(event)
    
    test.draw(node_editor)
    
    offset = (0,0)  # TODO: make it scrollable and bigger/longer than the actual screen (adaptable as needed?)
    screen.blit(node_editor, offset)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()