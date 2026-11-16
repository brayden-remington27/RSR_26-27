import pygame
from node import Node
from config import *

r = IO_PORTS_RADIUS

class Port:
    def __init__(self, pos: tuple[int,int], type: int, node: Node):
        self.pos = pos
        self.box = pygame.Rect((self.pos[0]*r, self.pos[1]*r), (r*2,r*2))  # used for collisions
    
    def draw(self, surface):
        pygame.draw.circle(surface, GRAY, self.box.center, r)