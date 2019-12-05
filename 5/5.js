// Module to load data from files.
const fs = require('fs');

// Import the computer.
const computer = require('../computer.js');

// Decide the filename.
let FILENAME = 'board.dat';
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
            // Parse the data into a board of numbers.
            let numbers = data.toString().split('\n')[0].split(',');
            let board = [];
            for (number of numbers)
            {
                board.push(parseInt(number, 10));
            }

            // Execute the instructions in the board.
            computer.execute(board);
        }
    })
}