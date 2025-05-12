"""
Title:  Escalation
Author:  Matthew Kenyon
Date:  2025-05-07
Version:  indev
Purpose:  Get a engine working for file loading and tracking movement.
"""

from maze_lib import load_maze, print_maze, maze_setup

maze_file = "./mazes/1.txt"
avatar = [1, 2, "ඞ"]  # row colum Representation
goal = [2, 3, "G"]  # row colum Representation
maze = load_maze(maze_file)


def move(avatar, maze):
    """change position of avatar"""
    # add code to move  avatar
    pass


def play_game(avatar, goal, MAZE):
    """main game loop"""
    while not (avatar[0] == goal[0] and avatar[0] == goal[0]):
        pass
    print("congratulations")


if __name__ == "__main__":
    test_maze = maze_setup(maze, goal, avatar)
    print_maze(test_maze)
