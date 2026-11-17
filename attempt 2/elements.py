import pygame
from config import *

class Element:
    def __init__(self, box: pygame.Rect):
        self.box = box
        
        self.hovered = self.box.collidepoint(pygame.mouse.get_pos())
        self.L_clicked = False
        self.R_clicked = False
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.box.collidepoint(event.pos)        # update status if mouseover object
            if self.hovered:
                self.hovering()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.box.collidepoint(event.pos):                   # not checking hovering to make sure -- mousedown can regester before motion
                if event.button == 1:                               # left click
                    self.L_clicked = True
                    self.L_clicking()                               # use the button functionality
                elif event.button == 3:                             # right click (3)
                    self.R_clicked = True
                    self.R_clicking()
        
        elif event.type == pygame.MOUSEBUTTONUP:
            self.unclicking()
            self.L_clicked = False
            self.R_clicked = False
    
    def hovering(self):
        pass
    
    def L_clicking(self):
        pass
    
    def R_clicking(self):
        pass
    
    def unclicking(self):
        pass
    
    def update(self):
        pass
    
    def draw(self, surface: pygame.Surface, fill: tuple[int,int,int], border: tuple[int,tuple[int,int,int]] = (0,(0,0,0)), radius: int=0):
        pygame.draw.rect(surface, fill, self.box, border_radius=radius)  # fill
        if border[0]:  # if there's a border
            pygame.draw.rect(surface, border[1], self.box, width=border[0], border_radius=radius)  # border
    
class Node(Element):
    def __init__(self, title: str, pos: tuple[int,int], color: tuple[int,int,int], nIO: tuple[int,int] = [0,0]):
        self.title = title
        self.color = color
        self.nIO = nIO  # mostly needed for external reference
        
        self.text_surface = FONT.render(self.title, ANTIALIAS, TEXT_COLOR)
        
        # automatically define size from the text size
        size = (self.text_surface.get_width()+TEXT_BUFFER[0], self.text_surface.get_height()+TEXT_BUFFER[1])  # not needed beyond box init nor pos
        
        super().__init__(pygame.Rect(pos, size))


        self.b_color = tuple([((c - 30) % 256) for c in self.color])  # loops back around
    def draw(self, surface: pygame.Surface):
        super().draw(surface, self.color, (NODE_BORDER_WIDTH, self.b_color), NODE_BORDER_RADIUS)  # the buffer is already built in from before
        surface.blit(self.text_surface, self.text_surface.get_rect(center=self.box.center))  # title
        
    
    def update(self):  # for things that need to run constantly but aren't drawn nor triggered
        if self.L_clicked:
            self.box.center = pygame.mouse.get_pos()

class Button(Element):
    def __init__(self, box: pygame.Rect, color: tuple[int,int,int], title: str=None, callback=None):
        super().__init__(box)
        
        self.callback = callback
        self.color = color
        self.title = title
        
        self.text_surface = FONT.render(self.title, ANTIALIAS, TEXT_COLOR)
    
    def draw(self, surface):
        super().draw(surface, self.color)
        if self.title:
            surface.blit(self.text_surface, self.text_surface.get_rect(center=self.box.center))  # title
    
    def L_clicking(self):  # run the assigned function
        if self.callback:
            self.callback()

# class Port(Element):
#     def __init__(self, box: pygame.Rect):
#         super().__init__(box)

# class Menu(Element):
#     def __init__(self, box: pygame.Rect):
#         super().__init__(box)

class Wire:  #(Element):
    def __init__(self, p1: tuple[int,int], p2: tuple[int,int]):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, surface):
        pygame.draw.line(surface, WIRE_COLOR, self.p1, self.p2, WIRE_WIDTH)