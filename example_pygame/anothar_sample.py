
# Importing the library
import pygame
  
# Initializing Pygame modules
pygame.init()
  
# Initializing surface
surface = pygame.display.set_mode((400,300))
  
# Initialing RGB Color 
color = (0, 0, 255)
  
# Changing surface color
surface.fill(color)
pygame.display.flip()