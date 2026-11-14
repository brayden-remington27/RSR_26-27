import pygame

class Widget:
    def __init__(self, box: pygame.Rect, clickable, draggable):
        self.box = box
        self.clickable = clickable
        self.draggable = draggable
        
        # states
        self.hovering = False
        # self.clicking = False
        self.dragging = False
        self.dragOffset = (0,0)
    
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
                    #print("regestered")
                    if self.clickable:
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
    def draw(self):
        pass