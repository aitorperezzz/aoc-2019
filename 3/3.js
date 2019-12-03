// Module to load data from a file.
const fs = require('fs');

const FILENAME = 'input.dat';

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

    // Transform each set of points into a set of segments.
    let segments1 = [], segments2 = [];
    fillSegments(positions1, segments1);
    fillSegments(positions2, segments2);

    // Declare the initial point of departure of the two wires.
    let initialPosition = {
        x: 0,
        y: 0
    };

    // Declare an initial closest intersection for the algorithm and minimal distance.
    let closestIntersection = {
        x: 0,
        y: 0
    };
    let minDistance = Infinity;

    // Traverse the first wire.
    let intersection;
    for (segment1 in segments1)
    {
        // Check if this one element is found in the other wire's array of positions.
        for (segment2 in segments2)
        {
            intersection = intersect(segment1, segment2);
            if (intersection != undefined)
            {
                if (manhattanDistance(intersection, initialPosition) < minDistance)
                {
                    // Update the optimal position.
                    minDistance = manhattanDistance(intersection, initialPosition);
                    closestIntersection.x = intersection.x;
                    closestIntersection.y = intersection.y;
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

    // Follow each of the instructions.
    for (let i = 0; i < instructions.length; i++)
    {
        // Select a proper velocity based on the letter of the instruction.
        switch (instructions[i].letter)
        {
            case 'U':
                positions.push({
                    x: positions[numberPositions].x,
                    y: positions[numberPositions].y + instructions[i].steps
                });
                break;
            case 'D':
                positions.push({
                    x: positions[numberPositions].x,
                    y: positions[numberPositions].y - instructions[i].steps
                });
                break;
            case 'R':
                positions.push({
                    x: positions[numberPositions].x + instructions[i].steps,
                    y: positions[numberPositions].y
                });
                break;
            case 'L':
                positions.push({
                    x: positions[numberPositions].x - instructions[i].steps,
                    y: positions[numberPositions].y
                });
                break;
            default:
                console.log('The letter ' + instructions[i].letter + ' of the instruction was not recognised!');
                return 1;
        }

        numberPositions++;
    }

    return 0;
}

function fillSegments(positions, segments)
{
    for (let i = 0; i < positions.length - 1; i++)
    {
        segments.push({
            initialx: positions[i].x,
            initialy: positions[i].y,
            finalx: positions[i + 1].x,
            finaly: positions[i + 1].y,
        });
    }
}

// Decides if two segments intersect and gives the intersection point.
function intersect(segment1, segment2)
{
    if (segment1.initialy == segment1.finaly)
    {
        // Segment 1 is vertical
    }
}

// Calculates the manhattan distance between two positions.
function manhattanDistance(position1, position2)
{
    return Math.abs(position1.x - position2.x) + Math.abs(position1.y - position2.y);
}