import pygame
from config import *

class Widget:
    def __init__(self, box: pygame.Rect, color, clickable, draggable):
        self.box = box
        self.clickable = clickable
        self.draggable = draggable
        self.color = color
        
        # states
        self.hovering = False
        # self.clicking = False
        self.dragging = False
        self.dragOffset = (0,0)
        
        ### Colors
        # border is themeColor-30, wrapped. somehow this works cuz python wraps -1 to 255 with %. nice.
        self.cFill = self.color
        self.cBorder = tuple([((c - 30) % 256) for c in self.color])
    
    def handleEvent(self, event):  # takes given event from pygame input loop to process it for any 
        # if event:
        #     print(event)
        if event.type == pygame.MOUSEMOTION:
            self.hovering = self.rect.collidepoint(event.pos) # update status if mouseover object
            if self.dragging and self.draggable:  # avoiding nesting multiple identical event checks with the statuses
                self.box.x = event.pos[0] + self.dragOffset[0]  # if mousedown, update the box accordingly
                self.box.y = event.pos[1] + self.dragOffset[1]
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):  # not checking hovering to make sure -- mousedown can regester before motion
                if event.button == 1:
                    if self.clickable:
                        #print("regestered")
                        self.clicked() # use the button functionality
                    if self.draggable:
                        self.dragging = True
                    self.dragOffset = (
                        self.box.x - event.pos[0],  # make the updates from the mouse
                        self.box.y - event.pos[1]
                    )
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.dragging:
                self.dragging = False
    
    def clicked(self):
        pass
    
    # TODO: evaluate if a universal drawing function is more effective or if I should leave it to the subclasses
    def draw(self, surface, cFill, cBorder):
        # main body
        pygame.draw.rect(surface, cFill, self.rect, border_radius=CORNER_RADIUS)  # fill
        pygame.draw.rect(surface, cBorder, self.rect, width=LINE_WIDTH, border_radius=CORNER_RADIUS)  # border