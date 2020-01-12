# Import modules.
import math

# Decide the name of the input file.
FILENAME = 'input.dat'

def main():
    # Calculate results and print them to the terminal.
    result = fuelForAllModules(FILENAME)

    print('Fuel required as per part one: {}'.format(result['fuel']))
    print('Fuel required as per part two: {}'.format(result['totalFuel']))


# Receives the name of an input file and calculates fuel required for all modules
# listed inside that file, in both ways (part one and part two).
def fuelForAllModules(fileName):
    with open(fileName, 'r') as file:
        masses = file.readlines()

    fuel = 0
    totalFuel = 0
    for mass in masses:
        fuel += calculateFuelMass(mass)
        totalFuel += calculateTotalFuelMass(mass)

    return {'fuel':fuel, 'totalFuel':totalFuel}

# Calculates the fuel required for a mass as per part one.
def calculateFuelMass(mass):
    return math.floor(int(mass) / 3) - 2

# Calculates the total fuel mass required as per part two.
def calculateTotalFuelMass(mass):
    fuelRequired = calculateFuelMass(mass)
    return fuelRequired + calculateTotalFuelMass(fuelRequired) if fuelRequired >= 0 else 0

# Call main function.
if __name__ == '__main__':
    main()