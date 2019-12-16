import sys
import math

# Select the name of the file to load.
FILENAME = 'input.dat'

# Class for a planet's info.
class Planet():
    def __init__(self):
        self.parent = None
        self.children = []

def distanceToCOM(originName, planetList):
    planet = planetList[originName]

    if planet.parent == None:
        # We found the COM point, the only one without parent.
        return 0
    else:
        # Recursively find the distance.
        return 1 + distanceToCOM(planet.parent, planetList)

# Gets the orbit information from a file and parses it to
# a dictionary.
def parseData(fileName):
    # Open the file and extract the orbits.
    with open(fileName, 'r') as file:
        orbits = file.readlines()

    # Parse the orbits into a dict of planet informations.
    planetDict = {}
    for orbit in orbits:
        # Get the names of the planet and the child.
        planetName = orbit.split(')')[0]
        childName = orbit.split(')')[1].rstrip('\n')

        # Create the child planet if it does not yet exist.
        if not childName in planetDict:
            planetDict[childName] = Planet()

        # Set the name of the parent.
        planetDict[childName].parent = planetName

        # Create the parent planet if it does not yet exist.
        if not planetName in planetDict:
            planetDict[planetName] = Planet()
        
        # Set the child of the parent planet.
        planetDict[planetName].children.append(childName)

    return planetDict

# Implements Djikstra algorithm to find the shortest path between
# origin and destination.
def dijkstra(planetDict, origin, destination):
    # Tentative distance dictionary. All have infinity in the start
    # except for origin, which has 0.
    distanceUnvisited = {}

    # Dictionary with the previous node for each node.
    previous = {}

    # Add all planets to the unvisited list, with infinity distance.
    for planet in planetDict:
        distanceUnvisited[planet] = math.inf

    # The origin needs to have zero distance.
    distanceUnvisited[origin] = 0

    # Go through the unvisted set.
    while distanceUnvisited:
        # Select the node with minimal distance among the unvisited.
        current = min(distanceUnvisited, key=distanceUnvisited.get)
        currentDistance = distanceUnvisited[current]

        # Check if this is the final node.
        if current == destination:
            return currentDistance

        # Remove this node from the unvisited list.
        del distanceUnvisited[current]

        # Get all the neighbors of the current node.
        neighbors = planetDict[current].children.copy()
        neighbors.append(planetDict[current].parent)

        # Iterate over all the neighbors of the current node.
        for neighbor in neighbors:
            # Only the ones that are unvisited.
            if neighbor in distanceUnvisited:
                # Get new estimate for the distance.
                dist = currentDistance + 1
                if dist < distanceUnvisited[neighbor]:
                    distanceUnvisited[neighbor] = dist
                    previous[neighbor] = current

def solveProblem(fileName):
    # Parse the data to a dictionary.
    planetDict = parseData(fileName)

    # Calculate the total of orbits.
    count = 0
    for planet in planetDict:
        # Sum the distance to COM of this object.
        count = count + distanceToCOM(planet, planetDict)

    # Calculate the shortest path between YOU and SAN.
    shortestPath = dijkstra(planetDict, 'YOU', 'SAN')

    return {'orbits':count, 'shortest':shortestPath}

# Solve the problem, part one and part two.
result = solveProblem(FILENAME)
print('Sum of direct and indirect orbits: {}'.format(result['orbits']))
print('Shortest path between YOU and SAN: {}'.format(result['shortest']))
