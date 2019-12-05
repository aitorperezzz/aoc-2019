// Define the exports of this module.
exports.execute = execute;
exports.print = print;

// Receives a reference to an array of ints that represents the program and executes 
// the instructions.
function execute(board)
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
                // Return the value in the first position to the caller.
                return board[0];
            default:
                console.log('Error: opcode ' + board[position] + ' not recognised!');
                return undefined;
        }
    }
}

function print(board)
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

// Executes the sum operation.
function executeSum(board, position1, position2, destination)
{
    board[destination] = board[position1] + board[position2];
}

// Executes the product operation.
function executeProduct(board, position1, position2, destination)
{
    board[destination] = board[position1] * board[position2];
}