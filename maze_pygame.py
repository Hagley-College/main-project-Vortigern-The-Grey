import pygame
import sys
from maze_lib import load_maze, maze_setup_goal, maze_setup_avatar_return, move

# Initialize Pygame
pygame.init()

# Screen dimensions
TILE_SIZE = 32
SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load sprites from /sprites folder
