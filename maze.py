"""
Title:  Escalation
Author:  Matthew Kenyon
Date:  2025-05-07
Version:  indev
Purpose:  Get a engine working for file loading and tracking movement.
"""

from maze_lib import load_maze, play_game

maze_file = "./mazes/1.txt"
avatar_row = 0  # Initial coordinates of player
avatar_column = 0
goal = [2, 3, "G"]  # Coordinates and character of goal
maze = load_maze(maze_file)  # Loads maze fro maze_file


if __name__ == "__main__":
    play_game(avatar_row, avatar_column, goal, maze)
