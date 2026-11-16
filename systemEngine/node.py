import pygame
from UIElement import Widget
#from port import Port
from config import *

class Node(Widget):
    def __init__(self, name: str, initPos: tuple[int,int], color: tuple[int,int,int], IO: list[int,int]=[0,0], callback=None):
        self.name = name
        self.initPos = initPos
        self.IO = IO
        self.callback = callback
        
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
            clickable=[False,True],
            draggable=True
        )
        
        
        
        #for i in range(1, self.IO[0]+1):
            
        #for i in range(1, self.IO[1]+1):
            
        
        self.inPortBoxOffsets = [
            (((self.size[0]/self.IO[0])*(i-0.5) ), 0) 
            for i in range(1, self.IO[0]+1)
        ]
        # Output Circle Nodes
        self.outPortBoxOffsets = [
            (((self.size[0]/self.IO[1])*(i-0.5) ), self.size[1]) 
            for i in range(1, self.IO[1]+1)
        ]
    
    def rClicked(self):
        #print("callbacked")
        if self.callback:
            self.callback(self)  # passes itself into the delNode function
    
    def draw(self, surface):
        # draw the ports circles
        for i in self.inPortBoxOffsets: pygame.draw.circle(surface, GRAY, (self.rect.x+i[0], self.rect.y+i[1]), IO_PORTS_RADIUS)  # input fill
        for i in self.outPortBoxOffsets: pygame.draw.circle(surface, GRAY, (self.rect.x+i[0], self.rect.y+i[1]), IO_PORTS_RADIUS)  # output fill
        
        super().draw(surface, self.cFill, self.cBorder)
        # text label/title
        text_rect = self.text_surface.get_rect(center=self.rect.center)
        surface.blit(self.text_surface, text_rect)