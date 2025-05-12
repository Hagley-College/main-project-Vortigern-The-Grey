"""
Title:  Escalation
Author:  Matthew Kenyon
Date:  2025-05-07
Version:  indev
Purpose:  Get a engine working for file loading and tracking movement.
"""


def load_maze(file):
    maze_file = open(file, "r")
    maze_list = []
    for line in maze_file:
        maze_list.append(list(line.strip()))

    return maze_list


def print_maze(maze):
    """
    prints out maze to console w/h spacing
    -----------
    - Matthew -
    -----------
    """
    for row in maze:
        for tile in row:
            print(f"{tile} ", end="")
        print()
    pass


def maze_setup(maze, goal, avatar):
    # place goal in maze
    maze[goal[0]][goal[1]] = goal[2]

    # place avatar in bottom left corner
    maze_length = len(maze)
    maze[maze_length - 2][1] = avatar[2]
    return maze
