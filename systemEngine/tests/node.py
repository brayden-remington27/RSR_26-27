import pygame



class Node:
    def __init__(self, start_x, start_y):
        self.font = pygame.font.SysFont("Arial", 16)
        
        # Master anchor box
        self.rect = pygame.Rect(start_x, start_y, 120, 60)
        self.text_surf = self.font.render("BOT-01", True, (255, 255, 255))
        
        # State tracking for mouse dragging
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0

    def handle_event(self, event):
        """Processes clicks and releases specifically for this object."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left click
                # Check if mouse clicked inside the body
                if self.rect.collidepoint(event.pos):
                    self.dragging = True
                    # Calculate structural offset to avoid the object jumping to its top-left corner
                    self.offset_x = self.rect.x - event.pos[0]
                    self.offset_y = self.rect.y - event.pos[1]
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False

    def update_position(self, screen_w, screen_h):
        """Updates dragging state and bounds the rect within current window size."""
        if self.dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.rect.x = mouse_x + self.offset_x
            self.rect.y = mouse_y + self.offset_y

        # Bounding limits considering top window and side tires
        # Window sticks out 20px above top, tires stick out 15px below bottom
        min_x = 0
        max_x = screen_w - self.rect.width
        min_y = 20  
        max_y = screen_h - self.rect.height - 15

        # Force anchor positions to stay within calculated screen limits
        self.rect.x = max(min_x, min(self.rect.x, max_x))
        self.rect.y = max(min_y, min(self.rect.y, max_y))

    def draw(self, surface):
        # Shape A: Main Body
        pygame.draw.rect(surface, (50, 150, 250), self.rect)
        
        # Shape B: Top Window
        window_rect = pygame.Rect(self.rect.x + 30, self.rect.y - 20, 60, 20)
        pygame.draw.rect(surface, (200, 220, 255), window_rect)
        
        # Shape C & D: Wheels
        wheel1_pos = (self.rect.left + 25, self.rect.bottom)
        wheel2_pos = (self.rect.right - 25, self.rect.bottom)
        pygame.draw.circle(surface, (30, 30, 30), wheel1_pos, 15)
        pygame.draw.circle(surface, (30, 30, 30), wheel2_pos, 15)
        
        # Element E: Text Label
        text_rect = self.text_surf.get_rect(center=self.rect.center)
        surface.blit(self.text_surf, text_rect)
