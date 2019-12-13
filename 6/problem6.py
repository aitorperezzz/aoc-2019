# Class that has the name of the father orbit and child orbit.
# The child is the one that orbits the father.
class OrbitInfo():
    def __init__(self, father, child):
        self.father = father
        self.child = child

def distanceFromTo(origin, destination, orbitInfo):
    if origin == destination:
        return 0
    else:
        for info in orbitInfo:
            if info.child == origin:
                return 1 + distanceFromTo(info.father, destination, orbitInfo)

def calculateNumberOrbits(fileName):
    # Open the file and extract the orbits.
    with open(fileName, 'r') as file:
        orbits = file.readlines()

    # Parse the orbits into a list of orbit infos.
    orbitInfo = []
    for orbit in orbits:
        # Get the names of the father and child.
        father = orbit.split(')')[0]
        child = orbit.split(')')[1].rstrip('\n')

        # Add this info to the list of orbit infos.
        orbitInfo.append(OrbitInfo(father, child))

    # Total of direct and indirect orbits.
    direct = 0
    indirect = 0
    for info in orbitInfo:
        # One more direct orbit.
        direct = direct + 1

        # Calculate the distance to COM.
        distanceToCOM = distanceFromTo(info.child, 'COM', orbitInfo)

        # Only if COM is two steps away or more, add indirect orbits
        if distanceToCOM > 1:
            indirect = indirect + distanceToCOM - 1

    return direct + indirect

# Execute the script with the data provided.
result = calculateNumberOrbits('input.dat')
print('Sum of direct and indirect orbits: {}'.format(result))






