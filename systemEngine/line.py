import pygame
from config import *

pygame.Rect()

class Line:
    def __init__(self, p1: tuple[int,int], p2: tuple[int,int]):
        self.p1 = p1
        self.p2 = p2
        
    def draw(self, surface):
        pygame.draw.line(surface, LINE_COLOR, self.p1, self.p2, LINE_WIDTH)