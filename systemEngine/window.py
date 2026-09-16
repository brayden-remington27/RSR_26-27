import pygame
import sys
from node import Node

# Initialize Pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# 1. Enable window resizing using the pygame.RESIZABLE flag
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

# Create object
player = Node(100, 300)

running = True
while running:
    # 2. Get current surface dimension on every tick (handles live resize updates)
    current_w, current_h = screen.get_size()
    
    screen.fill((240, 240, 240))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # 3. Allow engine to register structural size switches gracefully
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            
        # Pass clicks down to our object
        player.handle_event(event)

    # Manage movement updates and boundary checking
    player.update_position(current_w, current_h)
    
    player.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
