import pygame

class Widget:
    def __init__(self, box: pygame.Rect, clickable, dragable):
        self.box = box
    
    def handle_events(self, event):  # takes given event from pygame input loop to process it for any 
        pass