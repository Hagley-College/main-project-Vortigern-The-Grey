"""
Title:  Escalation
Author:  Matthew Kenyon
Date:  2025-05-07
Version:  indev
Purpose:  Get a engine working for file loading and tracking movement.
"""

from maze_lib import *

maze_file = "./mazes/1.txt"
avatar = [1, 2, "ඞ"]  # row colum Representation
goal = [2, 3, "G"]  # row colum Representation
maze_og = load_maze(maze_file)
maze = maze_og


if __name__ == "__main__":
    play_game(avatar, goal, maze, maze_og)
