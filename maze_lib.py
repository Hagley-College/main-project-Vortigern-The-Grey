"""
Title:  Escalation
Author:  Matthew Kenyon
Date:  2025-05-07
Version:  indev
Purpose:  Get a engine working for file loading and tracking movement.
"""


def load_maze(file):
    """
    Loads maze from txt file and returns it as a list of lists.
    """
    maze_file = open(file, "r")
    maze_list = []
    for line in maze_file:
        maze_list.append(list(line.strip()))

    return maze_list


def print_maze(maze, avatar_row, avatar_column):
    """
    Prints out maze and avatar to console with spacing (No longer needed, use pygame frontend)
    """
    for row in range(len(maze)):
        for tile in range(len(maze[row])):
            if avatar_row == row and avatar_column == tile:
                print("ඞ ", end="")  # Hardcoded avatar character for humour
            else:
                print(
                    f"{maze[row][tile]} ", end=""
                )  # Prints maze character directly from object
        print()
    pass


def maze_setup_goal(maze, goal):
    """
    Places goal in maze object for later comparisons
    """
    maze[goal[0]][goal[1]] = goal[2]
    return maze


def maze_setup_avatar_return(maze, avatar_row, avatar_column):
    """
    Calculates bottom left coordinate for avatar placement, not overlaping with a wall.
    """
    maze_height = len(maze)
    avatar_row = maze_height - 2
    avatar_column = 1
    return avatar_row, avatar_column


def move(avatar_row, avatar_column, maze, direction):
    """
    Changes position of avatar, determining if a collision with a wall or goal will occur and accounting for that
    """
    if (
        direction != "up"
        and direction != "down"
        and direction != "left"
        and direction != "right"
    ):
        """Meant to catch all non valid direction values"""
        print("direction not valid (up, down, left, right)")

    # TODO: None of this works for some reason. Basically, collisions are non-existent.
    # NOTE: It's a string. A goddamn string. I hate python.
    else:
        """
        Big if-else tree for checking collisions and moving the avatar appropriately.
        """
        if direction == "up":
            if maze[avatar_row - 1][avatar_column] == "1":
                type(1)
                print("Can't move there bc wall")
            else:
                avatar_row = avatar_row - 1
                print("Moved up")
        elif direction == "down":
            if maze[avatar_row + 1][avatar_column] == "1":
                print("Can't move there bc wall")
            else:
                avatar_row = avatar_row + 1
                print("Moved down")
        elif direction == "right":
            if maze[avatar_row][avatar_column + 1] == "1":
                print("Can't move there bc wall")
            else:
                avatar_column = avatar_column + 1
                print("Moved right")
        elif direction == "left":
            if maze[avatar_row][avatar_column - 1] == "1":
                print("Can't move there bc wall")
            else:
                avatar_column = avatar_column - 1
                print("Moved left")
        else:
            """
            Self-deprecating error statement if invalid direction slips through.
            """
            print("like, wtf")
            print(f"value of direction variable: {direction}")
            print("Fix this Matthew you worthless sack of flesh")

        return avatar_row, avatar_column


def play_game(avatar_row, avatar_column, goal, maze):
    """
    Main game loop for terminal rendering
    """
    win = False
    """Call maze_setup and render first maze"""
    maze = maze_setup_goal(maze, goal)
    avatar_row, avatar_column = maze_setup_avatar_return(
        maze, avatar_row, avatar_column
    )
    print_maze(maze, avatar_row, avatar_column)
    while win is False:
        """
        Game loop diagram
        - Wait for input to set direction
        - Move avatar using direction
        - Mreate new maze using avatar and maze
        - Draw new maze
        """
        # Terminal input (will be replaced with pygame keyboard inputs)
        direction = input("up, down, left, right \n>>>")

        # Move character based on direction
        avatar_row, avatar_column = move(avatar_row, avatar_column, maze, direction)

        # Draw new maze with new coordinates
        print_maze(maze, avatar_row, avatar_column)

        # End loop if goal is reached
        if int(avatar_row) == int(goal[0]) and int(avatar_column) == int(goal[1]):
            win = True
        pass
    print("congratulations")
