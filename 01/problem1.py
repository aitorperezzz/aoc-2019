# Import modules.
import math

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

# Decide the name of the input file.
FILENAME = 'input.dat'

# Calculate the results of part one and two.
result = fuelForAllModules(FILENAME)

# Print the results to the terminal.
print('Fuel required as per part one: {}'.format(result['fuel']))
print('Fuel required as per part two: {}'.format(result['totalFuel']))