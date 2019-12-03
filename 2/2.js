// File system module to load data from files.
const fs = require('fs');

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

            // Execute the program inside the board.
            executeBoard(board);

            // Print the resulting board.
            printBoard(board);

            // Print the result wanted.
            console.log('\nResult: ' + getResult(board));
        }
    });
}

function executeBoard(board)
{
    let position = 0;
    while (position < board.length)
    {
        switch (board[position])
        {
            case 1:
                executeSum(board, board[position + 1], board[position + 2], board[position + 3]);
                position += 4;
                continue;
            case 2:
                executeProduct(board, board[position + 1], board[position + 2], board[position + 3]);
                position += 4;
                continue;
            case 99:
                return;
            default:
                console.log('Error: opcode ' + board[position] + ' not recognised!');
                return;
        }
    }
}

function printBoard(board)
{
    console.log('Current status of the board: ');
    let text = '';
    for (let i = 0; i < board.length; i++)
    {
        text += board[i];
        if (i != board.length - 1)
        {
            text += ',';
        }
    }

    console.log(text);
}

function executeSum(board, position1, position2, destination)
{
    board[destination] = board[position1] + board[position2];
}

function executeProduct(board, position1, position2, destination)
{
    board[destination] = board[position1] * board[position2];
}

function getResult(board)
{
    return board[0];
}