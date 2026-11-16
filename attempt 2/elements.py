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
    
    def draw(self, surface: pygame.Surface, fill: tuple[int,int,int], border: tuple[float,tuple[int,int,int]] = (0,(0,0,0)), radius: float=0):
        pygame.draw.rect(surface, fill, self.box, border_radius=radius)  # fill
        if border[0]:  # if there's a border
            pygame.draw.rect(surface, border[1], self.box, width=border[0], border_radius=radius)  # border
    
class Node(Element):
    def __init__(self, title: str, pos: tuple[int,int], color: tuple[int,int,int]):
        self.title = title
        self.pos = pos
        self.color = color
        
        self.text_surface = FONT.render(self.title, ANTIALIAS, TEXT_COLOR)
        
        # automatically define size from the text size
        self.size = (self.text_surface.get_width()+TEXT_BUFFER[0], self.text_surface.get_height()+TEXT_BUFFER[1])
        
        super().__init__(pygame.Rect(self.pos, self.size))


        self.b_color = tuple([((c - 30) % 256) for c in self.color])  # loops back around
    def draw(self, surface: pygame.Surface):
        super().draw(surface, self.color, (NODE_BORDER_WIDTH, self.b_color), NODE_BORDER_RADIUS)  # the buffer is already built in from before
        surface.blit(self.text_surface, self.text_surface.get_rect(center=self.box.center))  # title
        
    
    def update(self):  # for things that need to run constantly but aren't drawn nor triggered
        if self.L_clicked:
            self.box.center = pygame.mouse.get_pos()

# class Port(Element):
#     def __init__(self, pos):
#         super().__init__(pos)

# class Menu(Element):
#     def __init__(self, pos):
#         super().__init__(pos)

class Line:  #(Element):
    def __init__(self, p1: tuple[int,int], p2: tuple[int,int]):
        self.p1 = p1
        self.p2 = p2