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
            utils.parsePositions(instructions1, positions1);
            utils.parsePositions(instructions2, positions2);

            // Calculate the distance to the nearest intersection point.
            let distance = calculateMinDistance(positions1, positions2);
            console.log('Minimal distance between the two wires: ' + distance);
        }
    });
}

// Receives two wires and gives the distance from the initial common point
// to the nearest intersection point.
function calculateMinDistance(positions1, positions2)
{
    // Common point of departure of the two wires.
    let initialPosition = {
        x: 0,
        y: 0
    };

    // Declare an initial closest intersection for the algorithm and minimal distance.
    let closestIntersection = {
        x: undefined,
        y: undefined
    };
    let minDistance = Infinity;

    // Traverse the first wire.
    let intersection;
    for (let i = 1; i < positions1.length; i++)
    {
        // Check if this one element is found in the other wire's array of positions.
        for (let j = 1; j < positions2.length; j++)
        {
            // Check if both wires share the same position.
            if (utils.equalPosition(positions1[i], positions2[j]))
            {
                // Check if this point is closer than the previous intersection point.
                if (utils.manhattanDistance(positions1[i], initialPosition) < minDistance)
                {
                    // Update the optimal position.
                    minDistance = utils.manhattanDistance(positions1[i], initialPosition);
                    closestIntersection.x = positions1[i].x;
                    closestIntersection.y = positions1[i].y;
                }

                // Continue with the loop because one intersection has been found.
                break;
            }
        }
    }

    return minDistance;
}
