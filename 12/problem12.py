import math
import sys

FILENAME = 'input.dat'
if len(sys.argv) == 2:
    FILENAME = sys.argv[1]

# Class that stores the position and velocity of a moon.
class Moon():
    def __init__(self, x, y, z):
        self.position = [x, y, z]
        self.velocity = [0, 0, 0]

    def updatePosition(self):
        for i in range(3):
            self.position[i] += self.velocity[i]

    def totalEnergy(self):
        return self.pot() * self.kin()
    
    def pot(self):
        return sum(map(abs, self.position))

    def kin(self):
        return sum(map(abs, self.velocity))

    def copy(self):
        return Moon(self.position[0], self.position[1], self.position[2])

def main(fileName, steps):
    # Parse the input to four moon objects.
    moons = parseInput(fileName)

    # Get a copy of the inital state.
    initial = copyState(moons)

    # Run the simulation the number of steps provided.
    simulateSteps(moons, steps)

    # Get the total energy of the final system.
    energy = sum(map(lambda moon: moon.totalEnergy(), moons))
    print('Energy of the system after {} steps: {}'.format(steps, energy))

    # Calculate the number of steps to reach the initial state again,
    # on each dimension separately.
    periods = []
    for dimension in range(3):
        periods.append(stepsToRepeat(initial, dimension))
    
    # Find the lcm of the three periods.
    repeat = lcm(periods[0], lcm(periods[1], periods[2]))
    print('Number of steps to repeat the inital state: {}'.format(repeat))

    return {'energy':energy, 'repeat':repeat}

# Parse the content of the filename to a list of moons.
def parseInput(fileName):
    # Get the raw input.
    with open(fileName, 'r') as file:
        lines = file.readlines()
    
    # Parse it to moons.
    moons = []
    for line in lines:
        values = line.lstrip('<').rstrip('>\n').split(',')
        coords = []
        for value in values:
            coords.append(int(value[(value.find('=') + 1):]))
        moons.append(Moon(coords[0], coords[1], coords[2]))

    return moons

def copyState(moons):
    result = []
    for moon in moons:
        result.append(moon.copy())
    
    return result

# Least common multiple of two numbers.
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Simulates the motion of the moons for the given steps.
def simulateSteps(moons, steps):
    number = len(moons)
    time = 0
    while time < steps:
        # Make one step of the simulation.
        simulateOnce(moons, number)

        # Update the time count.
        time += 1

# Executes only one step of the simulation.
def simulateOnce(moons, number):
    # Apply gravity to update the velocities of the moons.
    for i in range(number):
        for j in range(i + 1, number):
            applyGravity(moons[i], moons[j])

        # Now that the velocity is updated, update the position.
        moons[i].updatePosition()
        

def applyGravity(moon1, moon2):
    for i in range(3):
        if moon1.position[i] < moon2.position[i]:
            moon1.velocity[i] += 1
            moon2.velocity[i] -= 1
        elif moon1.position[i] > moon2.position[i]:
            moon1.velocity[i] -= 1
            moon2.velocity[i] += 1

# Calculates the number of steps to repeat the same initial state
# in the specified dimension.
def stepsToRepeat(moons, dimension):
    number = len(moons)
    initialpos = []
    initialvel = []
    pos = []
    vel = []
    for moon in moons:
        initialpos.append(moon.position[dimension])
        pos.append(moon.position[dimension])
        initialvel.append(moon.velocity[dimension])
        vel.append(moon.velocity[dimension])

    steps = 0
    while True:
        # Apply one step of the simulation.
        for i in range(number):
            for j in range(i + 1, number):
                if pos[i] < pos[j]:
                    vel[i] += 1
                    vel[j] -= 1
                elif pos[i] > pos[j]:
                    vel[i] -= 1
                    vel[j] += 1
            pos[i] += vel[i]
        steps += 1

        # Check if we reached the inital state.
        equal = True
        for i in range(number):
            if pos[i] != initialpos[i]:
                equal = False
                break
            if vel[i] != initialvel[i]:
                equal = False
                break
        
        if equal:
            return steps

def equalStates(state1, state2, number):
    for i in range(number):
        for j in range(3):
            if state1[i].position[j] != state2[i].position[j]:
                return False
            if state1[i].velocity[j] != state2[i].velocity[j]:
                return False

    return True

if __name__ == '__main__':
    main(FILENAME, 1000)