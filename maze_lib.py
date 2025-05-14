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


def maze_setup_goal(maze, goal):
    # place goal in maze
    maze[goal[0]][goal[1]] = goal[2]
    return maze


def maze_setup_avatar(maze, avatar):
    # place avatar in bottom left corner
    maze_length = len(maze)
    maze[maze_length - 2][1] = avatar[2]
    return maze


def maze_new_draw(maze_og, avatar):
    maze_og[avatar[0]][avatar[1]] = avatar[2]
    return maze_og


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

        return avatar


def play_game(avatar, goal, maze, maze_og):
    """main game loop"""
    win = False
    """put maze_setup and first maze render here"""
    maze_og = maze_setup_goal(maze_og, goal)
    maze_first = maze_setup_avatar(maze_og, avatar)
    print_maze(maze_first)
    while win is False:
        """
        Game loop diagram
        wait for input to set direction
        move avatar using direction
        create new maze using avatar and maze_og
        draw new maze
        """
        # stopgap for maze input
        direction = input("up, down, left, right \n>>>")

        # move character
        avatar = move(avatar, maze_og, direction)

        # create new maze for rendering
        maze_new = maze_new_draw(maze_og, avatar)

        # draw new maze
        print_maze(maze_new)

        if int(avatar[0]) == int(goal[0]) and int(avatar[1]) == int(goal[1]):
            win = True
        pass
    print("congratulations")
