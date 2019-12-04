// Functions exported by this module.
exports.parseInstructions = parseInstructions;
exports.parsePositionsAndSteps = parsePositionsAndSteps;
exports.equalPosition = equalPosition;
exports.manhattanDistance = manhattanDistance;

// Transforms each raw instruction into an object with a letter and some steps.
function parseInstructions(rawInstructions, instructions)
{
    for (let i = 0; i < rawInstructions.length; i++)
    {
        instructions.push({
            letter: rawInstructions[i][0],
            steps: parseInt(rawInstructions[i].substr(1), 10)
        });
    }
}

// Transforms a set of instructions into a set of positions plus steps.
// These steps are steps taken to reach each position of the wire.
function parsePositionsAndSteps(instructions, positions)
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
                y: positions[numberPositions].y + velocity.y,
                steps: undefined
            });

            // Check if this position has been previously visited.
            for (let j = 0; j < numberPositions + 1; j++)
            {
                if (equalPosition(positions[j], positions[numberPositions + 1]))
                {
                    // This position had been previously visited, so get that value of steps.
                    positions[numberPositions + 1].steps = positions[j].steps;
                    break;
                }
            }

            // If this position was never visited, put the normal steps.
            if (positions[numberPositions + 1].steps == undefined)
            {
                positions[numberPositions + 1].steps = numberPositions + 1;
            }

            // Update the number of steps.
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