import pygame, sys
pygame.init()

from elements import *
from config import *
import threading



#------------------------------------------#
#                 LOAD/SAVE                #
#------------------------------------------#
saved_data = load()

nodes = saved_data["nodes"]
lines = saved_data["lines"]
buttons = {
    "save": Button(pygame.Rect(500, 500, 50, 50), (30, 100, 40), title="→]", callback=lambda: save(nodes))  # lambda lets me pass an arg into it as a callback. 
}
menus = {}

elements = {
    "nodes": nodes,
    "lines": lines,  # TODO: implement into save via a node-connections var per node instance
    "buttons": buttons,
    "menus": menus
}

# init screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()





#------------------------------------------#
#                 MAIN LOOP                #
#------------------------------------------#
running = True
while running:
    
    screen.fill(BACKGROUND_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # events for all elements
        for node in elements["nodes"]:
            node.handle_event(event)
        
        for button in elements["buttons"].values():
            button.handle_event(event)
            
    
    # draw and update all elements
    for node in elements["nodes"]:
        node.draw(screen)
        node.update()
    
    for button in elements["buttons"].values():
        button.draw(screen)
        node.update()

    # update display and tick
    pygame.display.flip()
    clock.tick(60)

# clean quit
pygame.quit()
sys.exit()