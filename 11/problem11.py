import sys
sys.path.append('../')
import computer
import math
import pdb

FILENAME = 'input.dat'

# Possible colors of a panel.
BLACK = 0
WHITE = 1

# Possible rotations of the robot.
LEFT = 0
RIGHT = 1

# Possible coordinates.
COORDINATE_X = 0
COORDINATE_Y = 1

# 2D vector with the capacity to move and rotate.
class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Receives a rotation and rotates this vector.
    def updateDirection(self, rotation):
        # Decide the angle of movement.
        angle = math.pi / 2 if rotation == LEFT else - math.pi / 2

        # Apply the rotation matrix.
        newx = self.x * math.cos(angle) - self.y * math.sin(angle)
        newy = self.x * math.sin(angle) + self.y * math.cos(angle)
        self.x = int(round(newx))
        self.y = int(round(newy))
    
    # Receives a direction of movement and updates the position.
    def changePosition(self, direction):
        self.x += direction.x
        self.y += direction.y

# This is the grid of panels the robot paints to.
class Grid():
    def __init__(self):
        self.panels = {}

        # Keep track of the size of the grid.
        self.minx = math.inf
        self.maxx = - math.inf
        self.miny = math.inf
        self.maxy = - math.inf

    def updateExtremeValues(self, value, coordinate):
        if coordinate == COORDINATE_X:
            if value < self.minx:
                self.minx = value
            if value > self.maxx:
                self.maxx = value
        elif coordinate == COORDINATE_Y:
            if value < self.miny:
                self.miny = value
            if value > self.maxy:
                self.maxy = value


def main(filename):

    # Solve part one of the problem. The robot starts at a black panel.
    result = paintHull(filename, BLACK)
    print('Number of panels painted at least once: {}'.format(result['paintings']))

    # Solve part two of the problem. The robot starts at a white panel.
    grid = paintHull(filename, WHITE)['grid']

    # Print all the panels in the grid.
    print('\nRegistration identifier painted by the robot:')
    for y in reversed(range(grid.miny, grid.maxy + 1)):
        for x in range(grid.minx, grid.maxx + 1):
            if x in grid.panels and y in grid.panels[x]:
                if grid.panels[x][y] == BLACK:
                    print('.', end='')
                else:
                    print('#', end='')
            else:
                print('.', end='')
        print('')


# Receives a starting color and executes the hull painting routine.
def paintHull(filename, startingColor):

    # Load the painting robot software.
    paintingRobotSoftware = computer.readProgramFromFile(filename)
    paintingRobotSoftware.printOutputs(False)

    # Set the initial position and direction of the robot.
    position = Vector(0, 0)
    direction = Vector(0, 1)
    
    # Set the inital panel to the color provided.
    grid = Grid()
    grid.panels[position.x] = {}
    grid.panels[position.x][position.y] = startingColor
    paintings = 1

    while True:

        # Look for the current panel in the grid. If there, grab its color.
        # If not there, add it to the list and set it black initially.
        currentPanelColor = None
        justCreated = False
        if not position.x in grid.panels:
            grid.panels[position.x] = {}
            grid.updateExtremeValues(position.x, COORDINATE_X)
        if position.y in grid.panels[position.x]:
            currentPanelColor = grid.panels[position.x][position.y]
        else:
            grid.panels[position.x][position.y] = BLACK
            grid.updateExtremeValues(position.y, COORDINATE_Y)
            currentPanelColor = BLACK
            justCreated = True

        # Set the input for the program and empty the outputs.
        paintingRobotSoftware.emptyOutputs()
        paintingRobotSoftware.setInputs([currentPanelColor])
        paintingRobotSoftware.returnOnOutputNumber(2)

        # Execute and grab the output.
        result = paintingRobotSoftware.execute()
        outputs = paintingRobotSoftware.getOutputs()
        if result == computer.FINISH_HALT:
            break

        # Paint the panel.
        grid.panels[position.x][position.y] = outputs[0]
        if justCreated:
            paintings += 1

        # Update the direction and the position of the robot.
        direction.updateDirection(outputs[1])
        position.changePosition(direction)
    
    return {'paintings':paintings, 'grid':grid}

if __name__ == '__main__':
    main(FILENAME)
