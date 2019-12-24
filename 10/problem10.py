import math
import sys
from collections import defaultdict

# Decide the name of the file.
FILENAME = 'input.dat'
if len(sys.argv) == 2:
    FILENAME = sys.argv[1]


class Place():
    def __init__(self, i, j, asteroid):
        self.i = i
        self.j = j
        self.asteroid = asteroid
        self.visible = True

# Class to solve the second part. Stores info about the angle
# and the distance of an object to a monitoring station.
class AngleInfo():
    def __init__(self, x, y, xstation, ystation):
        self.x = x
        self.y = y
        self.angle = angle(xstation, ystation, x, y)
        self.dist = distance(xstation, ystation, x, y)


def main(fileName, full):
    # Get the input from the file.
    with open(fileName, 'r') as file:
        rawLines = file.readlines()
    
    # Parse the data into a list of asteroids.
    grid = parseRawInput(rawLines)

    # Find the best location for the station and print it.
    result = findBestLocation(grid)
    print('Best location for the station: ({},{})'.format(result['bestx'], result['besty']))
    print('Number of asteroids in sight: {}'.format(result['visibles']))

    if not full:
        return result

    # Find the location of the asteroid that gets vaporized the 200th.
    vaporized = findVaporized200(grid, result['bestx'], result['besty'])
    print('Asteroid vaporized in 200th place is at ({},{})'.format(vaporized['x'], vaporized['y']))

    # Add to the results.
    result['vaporizedx'] = vaporized['x']
    result['vaporizedy'] = vaporized['y']
    return result

# Parse raw lines to a list of asteroid objects.
def parseRawInput(lines):
    asteroids = []
    number = 0

    for i in range(len(lines)):
        asteroids.append([])
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                number += 1
                asteroids[i].append(Place(i, j, True))
            elif lines[i][j] == '.':
                asteroids[i].append(Place(i, j, False))

    return {'asteroids':asteroids, 'number':number, 'idim':len(asteroids), 'jdim':len(asteroids[0])}


# Receives a double array of asteroids and finds the best location
# for a station and the number of asteroids visible from there.
def findBestLocation(grid):
    asteroids = grid['asteroids']
    number = grid['number']
    idim = grid['idim']
    jdim = grid['jdim']

    # Number of asteroids visible from the best spot.
    bestVisibles = -1

    # Go through all asteroids checking the number of visibles from each one.
    for i in range(idim):
        for j in range(jdim):

            # Only analyze asteroids.
            if not asteroids[i][j].asteroid:
                continue

            # Grab a copy of asteroids as the testing ones.
            # Set the number of visibles to the initial value.
            testing = []
            copyBoard(asteroids, testing, idim, jdim)
            visibles = number - 1

            # Go through all the testing asteroids and remove the ones
            # blocked by those.
            for iblocking in range(idim):
                for jblocking in range(jdim):

                    # Skip if this is the original asteroid.
                    if i == iblocking and j == jblocking:
                        continue

                    # Skip if this is not an asteroid or not visible.
                    if not testing[iblocking][jblocking].asteroid or not testing[iblocking][jblocking].visible:
                        continue

                    # Calculate the steps in i and j.
                    gcd = math.gcd(abs(iblocking - i), abs(jblocking - j))
                    istep = int((iblocking - i) / gcd) if gcd != 0 else int(iblocking - i)
                    jstep = int((jblocking - j) / gcd) if gcd != 0 else int(jblocking - j)

                    # Remove asteroids following the steps.
                    inext = iblocking + istep
                    jnext = jblocking + jstep
                    while inext >= 0 and inext < idim and jnext >= 0 and jnext < jdim:
                        if testing[inext][jnext].asteroid and testing[inext][jnext].visible:
                            testing[inext][jnext].visible = False
                            visibles -= 1
                        inext += istep
                        jnext += jstep

            # Update the best asteroid if needed.
            if visibles > bestVisibles:
                bestVisibles = visibles
                bestAsteroid = {'i':i, 'j':j}

    return {'bestx':bestAsteroid['j'], 'besty':bestAsteroid['i'], 'visibles':bestVisibles}

# Copies the origin board to destination.
def copyBoard(origin, destination, idim, jdim):
    for i in range(idim):
        destination.append([])
        for j in range(jdim):
            destination[i].append(Place(i, j, origin[i][j].asteroid))

# Prints a board of asteroids.
def printBoard(asteroids, idim, jdim):
    for i in range(idim):
        for j in range(jdim):
            if asteroids[i][j].asteroid and asteroids[i][j].visible:
                print('#', end='')
            else:
                print('.', end='')

        print()
    print()

# Receives the location of the monitoring station and finds the 
# asteroid that gets vaporized in 200th place.
def findVaporized200(grid, x, y):
    asteroids = grid['asteroids']
    idim = grid['idim']
    jdim = grid['jdim']

    # Get the coordinates of the station.
    istation = y
    jstation = x
    xstation = x
    ystation = idim - istation - 1

    # Parse an angle for each asteroid.
    angles = []
    for i in range(idim):
        for j in range(jdim):
            # Skip if not an asteroid or the asteroid is the station.
            if not asteroids[i][j].asteroid:
                continue
            if i == istation and j == jstation:
                continue

            # Create a new angle object and add it to the list.
            angles.append(AngleInfo(j, idim - i - 1, xstation, ystation))

    # Create a default dictionary, where each value, if it does not exist,
    # gets an empty list by default.
    anglesDict = defaultdict(list)
    for angle in angles:
        anglesDict[angle.angle].append(angle)

    # Transform the dict to a double list.
    finalList = [[k, v] for k, v in anglesDict.items()]

    # Order the previous list by value of the angle.
    finalList.sort()

    # Order the list for each angle by the distance to the station.
    for element in finalList:
        element[1].sort(key=orderByDistance)

    # Remove elements from the list following value of angle
    # and then distance to the station.
    vaporized = 0
    length = len(finalList)
    position = 0
    while vaporized < 200:
        if len(finalList[position][1]) != 0:
            last = finalList[position][1].pop(0)
            vaporized += 1
        position = (position + 1) % length
    
    # The asteroid vaporized in 200th place is the last one.
    return {'x':last.x, 'y':idim - last.y - 1}


# Given the position of the asteroid and the station, get the
# angle starting from vertical, clockwise.
def angle(xstation, ystation, x, y):
    # Calculate angle according to the standard system.
    if x - xstation == 0:
        angle = math.pi / 2 if y - ystation > 0 else - math.pi / 2
    elif x - xstation >= 0:
        angle = math.atan((y - ystation) / (x - xstation))
    else:
        angle = math.pi + math.atan((y - ystation) / (x - xstation))

    # Now transform this angle to start at zero at vertical and go clockwise.
    angle = math.pi / 2 - angle
    
    # Return the angle with a positive value.
    return angle if angle >= 0 else angle + 2 * math.pi


# Get the distance between the station and the asteroid.
def distance(xstation, ystation, x, y):
    return abs(x - xstation) + abs(y - ystation)

def orderByDistance(info):
    return info.dist

# Call the main function if the module is ran.
if __name__ == '__main__':
    main(FILENAME, full=True)