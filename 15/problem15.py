import sys
sys.path.append('../')
import computer
import pdb

# Define the different types of locations inside the grid.
LOCATION_TYPE_WALL = 0
LOCATION_TYPE_EMPTY = 1
LOCATION_TYPE_TANK = 2
LOCATION_TYPE_UNKNOWN = 3

# Define the four directions of movement for the robot.
MOVE_NORTH = 1
MOVE_SOUTH = 2
MOVE_WEST = 3
MOVE_EAST = 4
movements = [MOVE_NORTH, MOVE_SOUTH, MOVE_WEST, MOVE_EAST]

class Grid():

    def __init__(self):

        # Initialize the locations inside the grid.
        self.locations = {}

        # Keep track of the extreme values of the grid.
        self.miny = 0
        self.maxy = 0
        self.minx = 0
        self.maxx = 0

        # Define some symbols to print the grid.
        self.symbols = {
            LOCATION_TYPE_EMPTY: ' ',
            LOCATION_TYPE_WALL: '#',
            LOCATION_TYPE_TANK: 'O'
        }
    
    # Updates the extreme values of the grid whenever they are inserted.
    def updateMaximalValues(self, value, coordinate):
        if coordinate == 'x':
            if value > self.maxx:
                self.maxx = value
            if value < self.minx:
                self.minx = value
        elif coordinate == 'y':
            if value > self.maxy:
                self.maxy = value
            if value < self.miny:
                self.miny = value

class Location():
    def __init__(self, x, y, locationType=LOCATION_TYPE_UNKNOWN):
        self.x = x
        self.y = y
        self.type = locationType
    
    # Receives a movement and returns a new location moved.
    def move(self, movement):
        if movement == MOVE_EAST:
            return Location(self.x + 1, self.y)
        elif movement == MOVE_SOUTH:
            return Location(self.x, self.y - 1)
        elif movement == MOVE_WEST:
            return Location(self.x - 1, self.y)
        elif movement == MOVE_NORTH:
            return Location(self.x, self.y + 1)
        else:
            # The movement is not allowed.
            return None
    
    # Returns the movement needed to reach the specified location.
    def movementToReach(self, location):
        if self.x < location.x:
            return MOVE_EAST
        elif location.x < self.x:
            return MOVE_WEST
        elif location.y < self.y:
            return MOVE_SOUTH
        elif self.y < location.y:
            return MOVE_NORTH

def main(filename):

    controller = computer.readProgramFromFile(filename)
    controller.printOutputs(False)

    # Define the starting position of the robot.
    startLocation = Location(0, 0, LOCATION_TYPE_EMPTY)

    # Perform a flood fill algorithm to know the area around the
    # starting position.
    grid = Grid()
    floodFill(startLocation, grid, controller)

    #pdb.set_trace()
    for y in range(grid.miny, grid.maxy + 1):
        for x in range(grid.minx, grid.maxx + 1):
            locationType = None
            try:
                locationType = grid.locations[y][x].type
            except:
                locationType = LOCATION_TYPE_EMPTY
            print(grid.symbols[locationType], end='')
        print()


# Establishes a grid performing flood fill with the help
# of the robot controller.
def floodFill(currentLocation, grid, controller, lastLocation=None):
    #pdb.set_trace()
    # Return if this location has already been explored.
    if currentLocation.y in grid.locations:
        if currentLocation.x in grid.locations[currentLocation.y]:
            return False
    
    # Get this location inside the grid and mark its type.
    if not currentLocation.y in grid.locations:
        grid.locations[currentLocation.y] = {}
        grid.updateMaximalValues(currentLocation.y, 'y')
    if not currentLocation.x in grid.locations[currentLocation.y]:
        grid.locations[currentLocation.y][currentLocation.x] = currentLocation.type
        grid.updateMaximalValues(currentLocation.x, 'x')
    
    # If this is a wall, do not continue with the algorithm.
    if currentLocation.type == LOCATION_TYPE_WALL:
        return False
    
    # Perform flood fill in all four directions.
    for movement in movements:

        # Try to move the robot and get the result.
        controller.emptyOutputs()
        controller.setInputs([movement])
        controller.returnOnOutputNumber(1)
        controller.execute()
        result = controller.getOutputs()[0]
        '''if result != 1:
            pdb.set_trace()'''

        # Update the location based on the result.
        newLocation = currentLocation.move(movement)
        newLocation.type = result

        # Call flood fill on this new location.
        if floodFill(newLocation, grid, controller, currentLocation):
            return True
    
    # If all the cells around have been explored, backtrack.
    controller.setInputs([currentLocation.movementToReach(lastLocation)])
    controller.returnOnOutputNumber(1)
    controller.execute()
    
    return False

if __name__ == '__main__':
    main('controller.dat')