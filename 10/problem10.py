import math

FILENAME = 'input.dat'

class Asteroid():
    def __init__(self, i, j):
        self.i = i
        self.j = j

def main(fileName):
    # Get the input from the file.
    with open(fileName, 'r') as file:
        rawLines = file.readlines()
    
    # Parse the data into a list of asteroids.
    asteroids = parseRawInput(rawLines)

    # Find the result and print it.
    result = findBest(asteroids)
    print('Best location for the station: ({},{})'.format(result['bestx'], result['besty']))
    print('Number of asteroids in sight: {}'.format(result['number']))

    return result

# Parse raw lines to a double array of asteroids.
def parseRawInput(lines):
    asteroids = []

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                asteroids.append(Asteroid(i, j))

    return asteroids


# Receives a double array of asteroids and returns the best location
# for a station and the number of asteroids in sight.
def findBest(asteroids):
    # Number of asteroids visible from the best spot.
    bestNumVisibles = -1

    for asteroid in asteroids:

        #print('asteroide: ({},{})'.format(asteroid.i, asteroid.j))
        # Find the number of visible asteroids from this one.
        visiblesFromAsteroid = 0

        # Go through all the other asteroids and check if they're blocked by another.
        for candidate in asteroids:

            #print('\tcomprobando ({},{})'.format(candidate.i, candidate.j))

            # Do not check the same asteroid.
            if asteroid == candidate:
                continue

            gcd = math.gcd(abs(candidate.i - asteroid.i), abs(candidate.j - asteroid.j))
            if gcd == 0:
                # This candidate cannot be blocked.
                visiblesFromAsteroid += 1
                continue

            # Check if each of the other asteroids block the view.
            foundBlocking = False
            for blocking in asteroids:
                    if blocking == asteroid or blocking == candidate:
                        continue
                    elif asteroidBlockingAnother(asteroid, blocking, candidate):
                        # This is a blocking asteroid, break.
                        foundBlocking = True
                        break

            if not foundBlocking:
                visiblesFromAsteroid +=1
                continue
                '''
            # Calculate the indexes of blocking asteroids.
            gcd = math.gcd(abs(candidate.i - asteroid.i), abs(candidate.j - asteroid.j))
            if gcd != 0:
                # There can be asteroids in between, only in this case. Find steps
                istep = abs(candidate.i - asteroid.i) / gcd
                jstep = abs(candidate.j - asteroid.j) / gcd

                # Go through all the asteroids and check if any one blocks the candidate.
                foundBlocking = False
                for blocking in asteroids:
                    if blocking == asteroid or blocking == candidate:
                        continue
                    elif asteroidBlockingAnother(asteroid, blocking, candidate, istep, jstep):
                        # This is a blocking asteroid, break.
                        foundBlocking = True
                        break
                
                if not foundBlocking:
                    print('\t\tvisible')
                    visiblesFromAsteroid += 1
                else:
                    print('\t\tno visible')
            else:
                # The candidate is not blocked by any other asteroid.
                # Count it as visible.
                print('\t\tvisible')
                visiblesFromAsteroid += 1
                continue'''

        #print('Asteroide en ({},{})->{}'.format(asteroid.i, asteroid.j, visiblesFromAsteroid))

        # Update the best asteroid if needed.
        if visiblesFromAsteroid > bestNumVisibles:
            bestNumVisibles = visiblesFromAsteroid
            bestAsteroid = Asteroid(asteroid.i, asteroid.j)

        #print('Mejor asteroide en ({},{})->{}'.format(bestAsteroid.i, bestAsteroid.j, bestNumVisibles))

    return {'bestx':bestAsteroid.j, 'besty':bestAsteroid.i, 'number':bestNumVisibles}


# Decides if blocking is blocking asteroid according to the steps.
def asteroidBlockingAnother(asteroid, blocking, candidate):
    # Check if the coordinates are between bounds.
    middlei = min(asteroid.i, candidate.i) <= blocking.i and blocking.i <= max(asteroid.i, candidate.i)
    middlej = min(asteroid.j, candidate.j) <= blocking.j and blocking.j <= max(asteroid.j, candidate.j)
    if not (middlei and middlej):
        return False

    # Check the three points are alligned.
    return (asteroid.j - blocking.j) * (asteroid.i - candidate.i) == (asteroid.j - candidate.j) * (asteroid.i - blocking.i)



# Call the main function
if __name__ == '__main__':
    main(FILENAME)