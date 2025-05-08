"""
Title:
Author:
Date:
Version:
Purpose:
"""


class Maze:
    """A 2 dimensional maze"""

    avatar = (1, 2, "A")  # row colum Representation
    goal = (1, 3, "G")  # row colum Representation
    MAZE = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]

    def __init__():
        pass

    def print_maze(self, maze, avatar, goal):
        """prints out maze to standard io
        -----
        - AG-
        -----
        """
        # add code to print out maze
        pass

    def move(self, row, col):
        """change position of avatar"""
        # add code to move avatar
        pass

    def collision(self, object_a, object_b):
        return object_a[0] == object_b[0] and object_a[1] == object_b[1]


def play_game():
    """main game loop"""
    maze = Maze()
    while not maze.collision(maze.avatar, maze.goal):
        pass
    print("congratulations")


if __name__ == "__main__":
    play_game()
