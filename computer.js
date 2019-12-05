// Define the exports of this module.
exports.execute = execute;
exports.print = print;

// Jump information according to type.
const jump = {
    1: 4,
    2: 4,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 4,
    8: 4
};

// Synchronous reading of input from terminal.
const readlineSync = require('readline-sync');

// Receives a reference to an array of ints that represents the program and executes 
// the instructions.
function execute(board)
{
    let position = 0;
    let opcode;
    while (position < board.length)
    {
        // Parse the opcode at this position.
        opcode = parseOpcode(board[position]);

        // Decide according to the type of opcode.
        switch (opcode.type)
        {
            case 1:
                position = executeSum(board, opcode, position);
                break;
            case 2:
                position = executeProduct(board, opcode, position);
                break;
            case 3:
                position = executeInput(board, opcode, position);
                break;
            case 4:
                position = executeOutput(board, opcode, position);
                break;
            case 5:
                position = executeJumpIfTrue(board, opcode, position);
                break;
            case 6:
                position = executeJumpIfFalse(board, opcode, position);
                break;
            case 7:
                position = executeLessThan(board, opcode, position);
                break;
            case 8:
                position = executeEquals(board, opcode, position);
                break;
            case 99:
                // Finish execution.
                return 0;
            default:
                console.log('Error: opcode ' + opcode.type + ' not recognised!');
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

// Parses an opcode into a structure with all the information.
function parseOpcode(number)
{
    let info = {};
    
    // Extract the first two digits as the type of operation.
    info.type = number % 100;

    // For each of the infos about parameter mode, store in an array.
    info.modes = [];
    number = parseInt(number / 100, 10);
    while (number > 0)
    {
        info.modes.push(number % 10);
        number = parseInt(number / 10, 10);
    }

    return info;
}

// Return the appropriate value for a parameter according to the mode.
function parseParameter(board, mode, parameter)
{
    if (mode == 0 || mode == undefined)
    {
        // This parameter is in position mode.
        return board[parameter];
    }
    else
    {
        // It is in immediate mode.
        return parameter;
    }
}

function executeSum(board, opcode, position)
{
    board[board[position + 3]] =
        parseParameter(board, opcode.modes[0], board[position + 1]) + 
        parseParameter(board, opcode.modes[1], board[position + 2]);

    return position + jump[opcode.type];
}

function executeProduct(board, opcode, position)
{
    board[board[position + 3]] = 
        parseParameter(board, opcode.modes[0], board[position + 1]) *
        parseParameter(board, opcode.modes[1], board[position + 2]);

    return position + jump[opcode.type];
}

function executeInput(board, opcode, position)
{
    board[board[position + 1]] = parseInt(readlineSync.question('Input: '), 10);

    return position + jump[opcode.type];
}

function executeOutput(board, opcode, position)
{
    console.log('Output: ' + parseParameter(board, opcode.modes[0], board[position + 1]));

    return position + jump[opcode.type];
}

function executeJumpIfTrue(board, opcode, position)
{
    if (parseParameter(board, opcode.modes[0], board[position + 1]) != 0)
    {
        return parseParameter(board, opcode.modes[1], board[position + 2]);
    }
    else
    {
        // Jump the default.
        return position + jump[opcode.type];
    }
}

function executeJumpIfFalse(board, opcode, position)
{
    // If the value is 0, jump to the address specified in the parameter.
    if (parseParameter(board, opcode.modes[0], board[position + 1]) == 0)
    {
        return parseParameter(board, opcode.modes[1], board[position + 2]);
    }
    else
    {
        // Jump the default.
        return position + jump[opcode.type];
    }
}

function executeLessThan(board, opcode, position)
{
    if (parseParameter(board, opcode.modes[0], board[position + 1]) < parseParameter(board, opcode.modes[1], board[position + 2]))
    {
        board[board[position + 3]] = 1;
    }
    else
    {
        board[board[position + 3]] = 0;
    }

    return position + jump[opcode.type];
}

function executeEquals(board, opcode, position)
{
    if (parseParameter(board, opcode.modes[0], board[position + 1]) == parseParameter(board, opcode.modes[1], board[position + 2]))
    {
        board[board[position + 3]] = 1;
    }
    else
    {
        board[board[position + 3]] = 0;
    }

    return position + jump[opcode.type];
}