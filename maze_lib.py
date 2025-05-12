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


def list_test(rows):
    maze = []
    for row in range(rows):
        maze.append([])
    print(maze)


# code for learning about list of lists
# list_test(3)
# list_test(10)

# maze import testing
# test_maze_1 = load_maze("./mazes/1.txt")
# print(test_maze_1)
# print("Testing Complete")
