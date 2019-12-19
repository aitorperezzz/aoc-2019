import math

FILENAME = 'input.dat'

class Place():
    def __init__(self, i, j, asteroid):
        self.i = i
        self.j = j
        self.asteroid = asteroid
        self.visible = True

def main(fileName):
    # Get the input from the file.
    with open(fileName, 'r') as file:
        rawLines = file.readlines()
    
    # Parse the data into a list of asteroids.
    asteroids = parseRawInput(rawLines)

    # Find the result and print it.
    result = findBestLocation(asteroids['asteroids'], asteroids['number'])
    print('Best location for the station: ({},{})'.format(result['bestx'], result['besty']))
    print('Number of asteroids in sight: {}'.format(result['visibles']))

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

    return {'asteroids':asteroids, 'number':number}


# Receives a double array of asteroids and finds the best location
# for a station and the number of asteroids visible from there.
def findBestLocation(asteroids, number):

    # Keep the dimensions of the board.
    idim = len(asteroids)
    jdim = len(asteroids[0])

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

# Call the main function
if __name__ == '__main__':
    main(FILENAME)