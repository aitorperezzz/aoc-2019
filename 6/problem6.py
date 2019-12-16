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

def calculateNumberOrbits(fileName):
    # Open the file and extract the orbits.
    with open(fileName, 'r') as file:
        orbits = file.readlines()

    # Parse the orbits into a dict of planet informations.
    planetList = {}
    for orbit in orbits:
        # Get the names of the planet and the child.
        planetName = orbit.split(')')[0]
        childName = orbit.split(')')[1].rstrip('\n')

        # Create the child planet if it does not yet exist.
        if not childName in planetList:
            planetList[childName] = Planet()

        # Set the name of the parent.
        planetList[childName].parent = planetName

        # Create the parent planet if it does not yet exist.
        if not planetName in planetList:
            planetList[planetName] = Planet()
        
        # Set the child of the parent planet.
        planetList[planetName].children.append(childName)

    # Total of direct and indirect orbits.
    count = 0
    for planet in planetList:
        # Sum the distance to COM of this object.
        count = count + distanceToCOM(planet, planetList)

    return count

# Execute the script with the data provided.
result = calculateNumberOrbits('input.dat')
print('Sum of direct and indirect orbits: {}'.format(result))






