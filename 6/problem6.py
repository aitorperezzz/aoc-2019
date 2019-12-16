import sys
import math

# Select the name of the file to load.
FILENAME = 'input.dat'

# Class for a planet's info.
class Planet():
    def __init__(self):
        self.parent = None
        self.children = []


# Receives the name of a planet and calculates its distance to COM.
def distanceToCOM(origin, planetDict):
    planet = planetDict[origin]
    if planet.parent == None:
        # This is the COM point, the only one without a parent.
        return 0
    else:
        # Recursively find the distance.
        return 1 + distanceToCOM(planet.parent, planetDict)


# Gets the orbit information from a file and parses it to
# a planet dictionary.
def parseData(fileName):
    # Open the file and extract the orbits.
    with open(fileName, 'r') as file:
        orbits = file.readlines()

    # Parse the orbits into a dict of planet infos.
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
    # Dictionary with tentative distances for all unvisited nodes.
    unvisited = {}

    # Dictionary with the previous node for each node.
    previous = {}

    # Add all the planets to the unvisited dict, and set distance to infinity.
    for planet in planetDict:
        unvisited[planet] = math.inf

    # Now, the origin needs to have zero distance to start the algorithm.
    unvisited[origin] = 0

    # Go through the unvisited set.
    while unvisited:
        # Select the node with minimal distance among the unvisited.
        current = min(unvisited, key=unvisited.get)
        currentDistance = unvisited[current]

        # Check if this is the final node and return.
        if current == destination:
            return currentDistance

        # Remove this node from the unvisited set.
        del unvisited[current]

        # Select the neighbors of the current node.
        # These are planets orbiting and orbited by the current planet.
        neighbors = planetDict[current].children.copy()
        neighbors.append(planetDict[current].parent)

        # Iterate over all the neighbors of the current node.
        for neighbor in neighbors:
            # Only the ones that are unvisited.
            if neighbor in unvisited:
                # Get new estimate for the distance.
                dist = currentDistance + 1
                if dist < unvisited[neighbor]:
                    unvisited[neighbor] = dist
                    previous[neighbor] = current

    return None


# Solves the two parts of the problem given a filename.
def solveProblem(fileName, calculateDistance):
    # Parse the data to a dictionary.
    planetDict = parseData(fileName)

    # Calculate the total of orbits.
    count = 0
    for planet in planetDict:
        # Sum the distance to COM of this object.
        count = count + distanceToCOM(planet, planetDict)

    # Calculate the distance between YOU and SAN.
    if calculateDistance:
        distance = dijkstra(planetDict, 'YOU', 'SAN') - 2
    else:
        distance = None

    return {'orbits':count, 'shortest':distance}


# Solve the problem, part one and part two.
result = solveProblem(FILENAME, True)
print('Sum of direct and indirect orbits: {}'.format(result['orbits']))
print('Shortest path between YOU and SAN: {}'.format(result['shortest']))
