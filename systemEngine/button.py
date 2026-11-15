import pygame
from UIElement import Widget
from config import *

class Button(Widget):
    def __init__(self, name: str, initPos: tuple[int,int], color: tuple[int,int,int]):
        self.name = name
        self.initPos = initPos
        
        # generate font and text
        self.font = pygame.font.SysFont("Arial", 16)
        self.text_surface = self.font.render(self.name, True, (255, 255, 255))
        
        # generate poition and size from text size and initPos
        self.size = [self.text_surface.get_width()+EDGE_BUFFER[0], self.text_surface.get_height()+EDGE_BUFFER[1]]
        # generate main body bounding box
        self.rect = pygame.Rect(self.initPos[0], self.initPos[1], self.size[0], self.size[1])
        
        super().__init__(
            self.rect,
            color,
            clickable=False,
            draggable=True
        )