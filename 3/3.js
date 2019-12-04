// Module to load data from a file.
const fs = require('fs');

// Load the utils module.
const utils = require('./utils.js');

// Decide the name of the file to load.
let FILENAME = 'input.dat';
if (process.argv[2])
{
    FILENAME = process.argv[2];
}

// Solve the problem.
solveProblem(FILENAME);

function solveProblem(fileName)
{
    fs.readFile(fileName, (error, data) => {
        if (error)
        {
            throw error;
        }
        else
        {
            // We got proper input.
            let rawWires = data.toString().split('\n');
            for (let i = rawWires.length - 1; i >= 0; i--)
            {
                if (!rawWires[i])
                {
                    rawWires.splice(i, 1);
                }
            }

            // Create the array of raw instructions for each wire.
            let rawInstructions1 = rawWires[0].split(',');
            let rawInstructions2 = rawWires[1].split(',');

            // Parse the instructions for each wire.
            let instructions1 = [], instructions2 = [];
            utils.parseInstructions(rawInstructions1, instructions1);
            utils.parseInstructions(rawInstructions2, instructions2);

            // Fill the positions of each wire.
            let positions1 = [], positions2 = [];
            utils.parsePositionsAndSteps(instructions1, positions1);
            utils.parsePositionsAndSteps(instructions2, positions2);

            // Solve both problems at the same time.
            let results = getResults(positions1, positions2);
            console.log('Minimal distance between the two wires: ' + results.minDistanceValue);
            console.log('Minimal signal delay: ' + results.minDelayValue);
        }
    });
}

// Receives the positions of the two wires and calculates the results for day three.
function getResults(positions1, positions2)
{
    // Common point of departure of the two wires.
    let initialPosition = {
        x: 0,
        y: 0
    };

    // Declare an initial closest intersection for the algorithm and minimal distance.
    let minDistancePosition = {
        x: undefined,
        y: undefined
    };
    let minDistanceValue = Infinity;

    // Declare the intersection with minimal signal delay.
    let minDelayPosition = {
        x: undefined,
        y: undefined
    };
    let minDelayValue = Infinity;

    // Traverse the first wire.
    for (let i = 1; i < positions1.length; i++)
    {
        // First update the number of steps for this position.
        // Check if this one element is found in the other wire's array of positions.
        for (let j = 1; j < positions2.length; j++)
        {
            // Check if both wires intersect at this position.
            if (utils.equalPosition(positions1[i], positions2[j]))
            {
                // Check if this point is closer than the previous intersection point.
                if (utils.manhattanDistance(positions1[i], initialPosition) < minDistanceValue)
                {
                    // Update the optimal position.
                    minDistanceValue = utils.manhattanDistance(positions1[i], initialPosition);
                    minDistancePosition.x = positions1[i].x;
                    minDistancePosition.y = positions1[i].y;
                }

                // Check if this intersection point has better delay signal.
                if (positions1[i].steps + positions2[j].steps < minDelayValue)
                {
                    minDelayPosition.x = positions1[i].x;
                    minDelayPosition.y = positions1[i].y;
                    minDelayValue = positions1[i].steps + positions2[j].steps;
                }

                // Continue with the loop because one intersection has been found.
                break;
            }
        }
    }

    return {
        minDistanceValue: minDistanceValue,
        minDelayValue: minDelayValue,
    };
}
