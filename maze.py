"""
Title:  Escalation
Author:  Matthew Kenyon
Date:  2025-05-07
Version:  indev
Purpose:  Get a engine working for file loading and tracking movement.
"""

avatar = (1, 2, "ඞ")  # row colum Representation
goal = (1, 3, "G")  # row colum Representation
MAZE = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]


def print_maze(maze, avatar, goal):
    """prints out maze to standard io
    -----
    - AG-
    -----
    """
    # add code to print out maze
    pass


def move(ava, maze):
    """change position of avatar"""
    # add code to move  avatar
    pass


def play_game(avatar, goal, MAZE):
    """main game loop"""
    while not (avatar[0] == goal[0] and avatar[0] == goal[0]):
        pass
    print("congratulations")


if __name__ == "__main__":
    play_game(avatar, goal, MAZE)
