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
try:
    WALL_SPRITE = pygame.image.load("sprites/wall.png")
    PLAYER_SPRITE = pygame.image.load("sprites/player.png")
    PATH_SPRITE = pygame.image.load("sprites/path.png")
    GOAL_SPRITE = pygame.image.load("sprites/goal.png")
except pygame.error as e:
    print(f"Error loading sprites: {e}")
    print(
        "Please ensure 'wall.png', 'player.png', 'path.png', and 'goal.png' are in the /sprites directory."
    )
    sys.exit()


def draw_maze(screen, maze, avatar_row, avatar_column):
    """
    Draws the maze on the Pygame screen using sprites.
    Renders path/wall/goal first, then the player on top for transparency effect.
    """

    for row_idx, row in enumerate(maze):
        for col_idx, tile in enumerate(row):
            x = col_idx * TILE_SIZE
            y = row_idx * TILE_SIZE
            # Draw the background tile first (path, wall, or goal)
            if tile == "1":  # Wall
                screen.blit(WALL_SPRITE, (x, y))
            elif tile == "0":  # Path
                screen.blit(PATH_SPRITE, (x, y))
            elif tile == "G":  # Goal
                screen.blit(GOAL_SPRITE, (x, y))
            else:
                # Fallback for unknown tiles, might draw a path sprite
                screen.blit(PATH_SPRITE, (x, y))

    # After drawing all background tiles, draw the player on top
    player_x = avatar_column * TILE_SIZE
    player_y = avatar_row * TILE_SIZE
    screen.blit(PLAYER_SPRITE, (player_x, player_y))
