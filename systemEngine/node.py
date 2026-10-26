import pygame

LINE_WIDTH = 3
CORNER_RADIUS = 4
EDGE_BUFFER = (20, 20)  # Left/Right Top/Bottom 
BORDER_COLOR_OFFSET = 30  # Difference in color between fill and border - wrapped
IO_PORTS_RADIUS = 10
GRAY = (140,140,140)
DARK_GRAY = (140,140,140)

class Node:
    def __init__(self, name: str, initPos: tuple[int,int], cTheme: tuple[int,int,int], IO: list[int,int]=[0,0]):
        self.name = name
        self.cTheme = cTheme
        self.initPos = initPos
        self.IO = IO
        
        self.font = pygame.font.SysFont("Arial", 16)
        self.text_surface = self.font.render(self.name, True, (255, 255, 255))
        
        self.pos = [self.initPos[0], self.initPos[1]]
        self.size = [self.text_surface.get_width()+EDGE_BUFFER[0], self.text_surface.get_height()+EDGE_BUFFER[1]]
        
        # Main Body
        self.rect = pygame.Rect(self.initPos[0], self.initPos[1], self.size[0], self.size[1])
        
        ### Generates the center points for the connection nodes
        # Input Circle Nodes
        self.inPortBoxes = [(( self.pos[0] + (self.size[0]/self.IO[0])*(i-0.5) ), self.pos[1]) for i in range(1, self.IO[0])]
        # Output Circle Nodes
        self.outPortBoxes = [(( self.pos[0] + (self.size[0]/self.IO[1])*(i-0.5) ), self.pos[1]+self.size[1]) for i in range(1, self.IO[1])]
        
        # Colors
        # border is themeColor-30, wrapped. somehow this works cuz python wraps -1 to 255 with %. nice.
        self.cFill = cTheme
        self.cBorder = tuple([((c - 30) % 256) for c in cTheme]) 
        
    def draw(self, surface):
        # body
        pygame.draw.rect(surface, self.cFill, self.rect, border_radius=CORNER_RADIUS)  # fill
        pygame.draw.rect(surface, self.cBorder, self.rect, width=LINE_WIDTH, border_radius=CORNER_RADIUS)  # border
        
        # text label
        text_rect = self.text_surface.get_rect(center=self.rect.center)
        surface.blit(self.text_surface, text_rect)
        
        # ports
        for i in self.inPortBoxes: pygame.draw.circle(surface, GRAY, i, IO_PORTS_RADIUS)  # input fill
        for i in self.outPortBoxes: pygame.draw.circle(surface, GRAY, i, IO_PORTS_RADIUS)  # output fill