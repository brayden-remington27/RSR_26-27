import pygame
from UIElement import Widget
from config import *

class Button(Widget):
    def __init__(self, name: str, rect: pygame.Rect, color: tuple[int,int,int], callback=None):
        
        self.name = name
        self.callback = callback
        self.rect = rect
        
        super().__init__(
            self.rect,
            color,
            clickable=(True, False),
            draggable=False
        )
        
        self.cFill = self.color
        self.cBorder = tuple([((c - 30) % 256) for c in self.color])
        
    def clicked(self):
        #print("callbacked")
        if self.callback:
            self.callback()
    
    def draw(self, surface):
        super().draw(surface, self.cFill, self.cBorder)