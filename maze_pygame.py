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


def pygame_game_loop(initial_avatar_row, initial_avatar_column, goal, maze_data):
    """
    Main Pygame game loop.
    Handles rendering and user input for movement, using maze_lib for logic.
    """
    global SCREEN_WIDTH, SCREEN_HEIGHT

    # Setup maze and initial avatar position using maze_lib functions
    maze = maze_setup_goal(maze_data, goal)
    avatar_row, avatar_column = maze_setup_avatar_return(
        maze, initial_avatar_row, initial_avatar_column
    )

    # Determine screen dimensions based on maze size
    maze_width = len(maze[0])
    maze_height = len(maze)
    SCREEN_WIDTH = maze_width * TILE_SIZE
    SCREEN_HEIGHT = maze_height * TILE_SIZE

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Escalation")

    running = True
    win = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                direction = ""
                if event.key == pygame.K_UP:
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                elif event.key == pygame.K_LEFT:
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    direction = "right"

                if direction:
                    # Use the move function from maze_lib for collision and movement logic
                    new_avatar_row, new_avatar_column = move(
                        avatar_row, avatar_column, maze, direction
                    )
                    # Only update avatar position if move function indicates a change
                    if (new_avatar_row, new_avatar_column) != (
                        avatar_row,
                        avatar_column,
                    ):
                        avatar_row, avatar_column = new_avatar_row, new_avatar_column
                        print(
                            f"Avatar moved to: ({avatar_row}, {avatar_column})"
                        )  # For debugging

                    # Check for win condition after moving
                    if int(avatar_row) == int(goal[0]) and int(avatar_column) == int(
                        goal[1]
                    ):
                        win = True
                        running = False  # End game loop on win

        # Fill the background
        screen.fill(BLACK)

        # Draw the maze with the current avatar position
        draw_maze(screen, maze, avatar_row, avatar_column)

        # Update the display
        pygame.display.flip()

    if win:
        print("Congratulations! You reached the goal!")
        # You can add a win screen or message here in Pygame
        font = pygame.font.Font(None, 50)
        text = font.render("YOU WIN!", True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)  # Show win message for 3 seconds

    pygame.quit()
    sys.exit()
