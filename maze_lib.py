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


def move(avatar, maze, direction):
    """change position of avatar"""
    if (
        direction != "up"
        and direction != "down"
        and direction != "left"
        and direction != "right"
    ):
        """Meant to catch all non valid direction values"""
        print("direction not valid (up, down, left, right)")

    else:
        if direction == "up":
            if maze[avatar[0] - 1][avatar[1]] == 1:
                print("Can't move there bc wall")
            else:
                avatar[0] = avatar[0] - 1
        elif direction == "down":
            if maze[avatar[0] + 1][avatar[1]] == 1:
                print("Can't move there bc wall")
            else:
                avatar[0] = avatar[0] + 1
        elif direction == "left":
            if maze[avatar[0]][avatar[1] - 1] == 1:
                print("Can't move there bc wall")
            else:
                avatar[1] = avatar[1] - 1
        elif direction == "right":
            if maze[avatar[0]][avatar[1] + 1]:
                print("Can't move there bc wall")
            else:
                avatar[1] = avatar[1] + 1
        else:
            print("like, wtf")
            print(f"value of direction variable: {direction}")
            print("Fix this Matthew you worthless sack of flesh")

        return maze
