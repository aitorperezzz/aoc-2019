const fs = require('fs');

const FILENAME = 'input.dat';

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
            // Get the input data.
            let stringNumbers = data.toString().split('\n')[0].split('-');
            let numbers = [];
            for (number of stringNumbers)
            {
                numbers.push(parseInt(number, 10));
            }
            
            // Log the limits to the terminal.
            console.log('Range of numbers: ' + numbers[0] + '->' + numbers[1]);

            // Calculate the number of passwords.
            let result = calculate(numbers[0], numbers[1]);
            console.log('Number of passwords: ' + result);
        }
    });
}

function calculate(begin, end)
{
    // Variable to count the number of valid passwords.
    let count = 0;

    // Iterate over the range provided.
    for (let i = begin; i <= end; i++)
    {
        if (increasingOrder(i) && hasTwoEqualDigits(i))
        {
            // This number is valid, count one.
            count++;
        }
    }

    return count;
}

// Receives a number and decides if its digits are ordered.
function increasingOrder(number)
{
    let stringNumber = number.toString();
    for (let i = 0; i < stringNumber.length - 1; i++)
    {
        if (parseInt(stringNumber.charAt(i), 10) > parseInt(stringNumber.charAt(i + 1), 10))
        {
            return false;
        }
    }

    return true;
}

function hasTwoEqualDigits(number, strong)
{
    let stringNumber = number.toString();
    for (let i = 0; i < stringNumber.length - 1; i++)
    {
        if (parseInt(stringNumber.charAt(i), 10) == parseInt(stringNumber.charAt(i + 1), 10))
        {
            return true;
        }
    }

    return false;
}