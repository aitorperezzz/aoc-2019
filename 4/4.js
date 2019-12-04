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

            // Calculate the number of valid passwords.
            let result = calculate(numbers[0], numbers[1]);
            console.log('Number of passwords (weak condition): ' + result.weak);
            console.log('Number of passwords (strong condition): ' + result.strong);
        }
    });
}

function calculate(begin, end)
{
    // Variable to count the number of valid passwords.
    let weak = 0, strong = 0;

    // Iterate over the range provided.
    for (let i = begin; i <= end; i++)
    {
        if (increasingOrder(i))
        {
            if (hasTwoEqualDigits(i))
            {
                // The weak condition applies.
                console.log(i + ' valido debil');
                weak++;

                if (hasTwoEqualDigitsStrong(i))
                {
                    // The strong condition applies.
                    console.log(i + ' valido fuerte');
                    strong++;
                }
            }
        }
    }

    return {
        weak: weak,
        strong: strong
    };
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

function hasTwoEqualDigits(number)
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

function hasTwoEqualDigitsStrong(test)
{
    let stringNumber = test.toString();

    let repeated = 0;
    let number = undefined;

    for (let i = 0; i < stringNumber.length - 1; i++)
    {
        if (parseInt(stringNumber.charAt(i), 10) == parseInt(stringNumber.charAt(i + 1), 10))
        {
            number = parseInt(stringNumber.charAt(i), 10);
            if (number == parseInt(stringNumber.charAt(i), 10))
            {
                repeated++;
            }
        }
        else if (repeated == 1)
        {
            return true;
        }
        else
        {
            // The number has changed, reset variables.
            repeated = 0;
            number = undefined;
        }
    }

    return repeated == 1 ? true : false;
}