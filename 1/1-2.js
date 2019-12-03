// Import module to read data from files.
const fs = require('fs');

// Input filename.
const FILENAME = '1.dat';

// Solve the problem.
solveProblem(FILENAME);

function solveProblem(fileName)
{
    // Read asynchronously from the file.
    fs.readFile(fileName, (error, data) => {
        if (error) {
            throw error;
        }
        else {
            // Calculate the result.
            let result = processData(data.toString());
            console.log('Result: ' + result);
        }
    });
}

function processData(stringData)
{
    // Convert the string data into an array of numbers.
    let numbers = stringData.split('\n');

    let sum = 0;
    for (let i = 0; i < numbers.length; i++)
    {
        // Check the string is valid.
        if (numbers[i])
        {
            console.log('Current number: ' + numbers[i]);
            sum += calculateFuelForMass(parseInt(numbers[i], 10));
        }
    }

    return sum;
}

// Receive a mass and calculate the fuel required by it.
function calculateFuelForMass(mass)
{
    let fuel = Math.floor(mass / 3) - 2;
    return fuel > 0 ? fuel + calculateFuelForMass(fuel) : 0;
}