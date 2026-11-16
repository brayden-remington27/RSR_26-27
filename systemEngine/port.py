import pygame
from UIElement import Widget
from config import *

r = IO_PORTS_RADIUS

class Port(Widget):
    def __init__(self, pos: tuple[int,int], callback=None):
        self.pos = pos
        self.box = pygame.Rect((self.pos[0]*r, self.pos[1]*r), (r*2,r*2))  # used for collisions, centers the box on pos instead of corner
        self.callback = callback
        
        super().__init__(
            self.box,
            GRAY,
            clickable=(True, False),
            draggable=False
        )
    
    def clicked(self):
        #print("callbacked")
        if self.callback:
            self.callback(self)
    
    def draw(self, surface):
        pygame.draw.circle(surface, GRAY, self.box.center, r)

class inPort(Port):
    def __init__(self, pos: tuple[int,int], callback=None):
        super().__init__(pos, callback)

class outPort(Port):
    def __init__(self, pos: tuple[int,int], callback=None):
        super().__init__(pos, callback)