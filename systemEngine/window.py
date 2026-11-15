import pygame
import sys
import pickle
from config import *
from node import Node
from button import Button

# To-Do List:
# TODO: standardize all camelcase and snakecase to only snake case for convention's sake
# TODO: write function/class descriptors
# TODO: improve readability and understandability of comments

pygame.init()

nodes = [Node("Testing", (50,50), (100, 110, 130), [2, 3])]
def addNode():
    name = input("name: ")
    r = int(input("red: "))
    g = int(input("green: "))
    b = int(input("blue: "))
    inps = int(input("ins: "))
    outs = int(input("outs: "))
    
    nodes.append(Node(name, (50,50), (r,g,b), [inps, outs]))

def save():
    with open(CURRENT_SAVE, "wb") as file:
        pickle.dump(nodes, file)

# def regester():
#     print("regestered")


makeNode = Button("make", pygame.Rect(500,500,50,50), (100, 230, 100), callback=addNode)
saveConfig = Button("save", pygame.Rect(570,500,50,50), (230, 100, 100), callback=save)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
canvas = pygame.Surface((800, 600))  # scrollable surface on to which all the nodes and lines are drawn
clock = pygame.time.Clock()

running = True
while running:
    
    canvas.fill(CANVAS_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in nodes:  # nodes[0] is drawn last, its on top
                if i.rect.collidepoint(event.pos):  # goes through the list to only select the top one if multiple are on top of eachother
                    i.handleEvent(event)
                    break  # makes sure to only look at the topmost one
        else:
            for i in reversed(nodes): i.handleEvent(event)
        makeNode.handleEvent(event)
    
    for i in reversed(nodes): i.draw(canvas)  # first on top
    makeNode.draw(canvas)
    
    offset = (0,0)  # TODO: make it scrollable and bigger/longer than the actual screen (adaptable as needed?)
    screen.blit(canvas, offset)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()