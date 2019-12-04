// Module to load data from a file.
const fs = require('fs');

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

            // Parse the instructions of each wire.
            let wireInstructions1 = [], wireInstructions2 = [];
            parseWireInstructions(rawInstructions1, wireInstructions1);
            parseWireInstructions(rawInstructions2, wireInstructions2);

            // Calculate the distance from the beginning to the nearest intersection.
            let distance = calculateMinDistance(wireInstructions1, wireInstructions2);
            console.log('Minimal distance between the two wires: ' + distance);
        }
    });
}

// Transforms each raw instruction into an object with a letter and some steps.
function parseWireInstructions(rawInstructions, instructions)
{
    for (let i = 0; i < rawInstructions.length; i++)
    {
        instructions.push({
            letter: rawInstructions[i][0],
            steps: parseInt(rawInstructions[i].substr(1), 10)
        });
    }
}

// Receives two wires and gives the distance from the initial common point
// to the nearest intersection point.
function calculateMinDistance(instructions1, instructions2)
{
    // First transform each set of instructions into an array of points on a grid.
    let positions1 = [], positions2 = [];
    fillPositions(instructions1, positions1);
    fillPositions(instructions2, positions2);

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
            if (equalPosition(positions1[i], positions2[j]))
            {
                // Check if this point is closer than the previous intersection point.
                if (manhattanDistance(positions1[i], initialPosition) < minDistance)
                {
                    // Update the optimal position.
                    minDistance = manhattanDistance(positions1[i], initialPosition);
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

function fillPositions(instructions, positions)
{
    // Current number of elements in positions array.
    let numberPositions = 0;

    // Add the starting position to the positions array.
    positions.push({
        x: 0,
        y: 0
    });

    // Declare a velocity for each instruction.
    let velocity = {
        x: 0,
        y: 0
    };

    // Follow each of the instructions.
    for (let i = 0; i < instructions.length; i++)
    {
        // Select a proper velocity based on the letter of the instruction.
        switch (instructions[i].letter)
        {
            case 'U':
                velocity.x = 0;
                velocity.y = 1;
                break;
            case 'D':
                velocity.x = 0;
                velocity.y = -1;
                break;
            case 'R':
                velocity.x = 1;
                velocity.y = 0;
                break;
            case 'L':
                velocity.x = -1;
                velocity.y = 0;
                break;
            default:
                console.log('The letter ' + instructions[i].letter + ' of the instruction was not recognised!');
                return 1;
        }

        // Fill all positions following the velocity.
        for (let k = 0; k < instructions[i].steps; k++)
        {
            positions.push({
                x: positions[numberPositions].x + velocity.x,
                y: positions[numberPositions].y + velocity.y
            });
            numberPositions++;
        }
    }

    return 0;
}

// Decide if two positions are equal.
function equalPosition(position1, position2)
{
    return position1.x == position2.x && position1.y == position2.y;
}

// Calculates the manhattan distance between two positions.
function manhattanDistance(position1, position2)
{
    return Math.abs(position1.x - position2.x) + Math.abs(position1.y - position2.y);
}