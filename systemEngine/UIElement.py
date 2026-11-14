import pygame

class Widget:
    def __init__(self, box: pygame.Rect, clickable, draggable):
        self.box = box
        self.clickable = clickable
        self.draggable = draggable
        
        # states
        self.hovering = False
        self.clicking = False
        self.dragging = False
        self.dragOffset = (0,0)
    
    def handle_events(self, event):  # takes given event from pygame input loop to process it for any 
        if event == pygame.MOUSEMOTION:
            self.hovering = self.rect.collidepoint(event.pos) # update status if mouseover object
            if self.dragging and self.draggable:  # avoiding nesting multiple identical event checks with the statuses
                    self.box.x = event.pos[0] + self.dragOffset[0]  # if mousedown, update the box accordingly
                    self.box.y = event.pos[1] + self.dragOffset[1]
        
        elif event == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):  # not checking hovering to make sure -- mousedown can regester before motion
                if event.button == 1:
                    if self.clickable:
                        self.clicked()
                        if self.draggable:
                            self.dragging = True
                        self.dragOffset = (
                            self.box.x - event.pos[0],
                            self.box.y - event.pos[1],
                        )
        elif event == pygame.MOUSEBUTTONUP:
            pass
    
    def clicked():
        pass