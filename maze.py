import sys


class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action



class StackFrontier():

    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


class Maze():
    def __init__(self, filename):
        self.filename = filename
        with open(filename) as f:
            contents = f.read()
        # Validate start and goal
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")
        # Read grid
        rows = contents.splitlines()
        self.grid = []
        for row in rows:
            row = row.split()
            self.grid.append(row)
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        # Validate grid
        for row in self.grid:
            if len(row) != self.width:
                raise Exception("each row of the grid must have the same number of columns")
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] not in ["A", "B", " ", "#"]:

