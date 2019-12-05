// File system module to load data from files.
const fs = require('fs');

// Import module of the computer.
const computer = require('../computer.js');

// Name of the input file.
let FILENAME = 'input.dat';
if (process.argv[2])
{
    FILENAME = process.argv[2];
}

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
            // Convert to a string.
            let parsedData = data.toString();
            console.log('Program loaded from file: ');
            console.log(parsedData);

            // Transform into a matrix separating by commas.
            let board = parsedData.split(',');

            // Remove any unwanted elements in the array.
            for (let i = board.length - 1; i >= 0; i--)
            {
                if (!board[i])
                {
                    // Remove this element from the array.
                    board.splice(i, 1);
                }
                else
                {
                    // Transform it into an integer.
                    board[i] = parseInt(board[i], 10);
                }
            }

            // Execute the instructions in the board.
            computer.execute(board);

            // Print the resulting board.
            computer.print(board);

            // Print the result wanted.
            console.log('\nResult: ' + board[0]);
        }
    });
}