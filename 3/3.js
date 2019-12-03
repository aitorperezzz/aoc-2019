// Module to get data from a file.
const fs = require('fs');

const FILENAME = 'input.dat';

// Solve the problem.
solveProblem(FILENAME);


function solveProblem(fileName)
{
    fs.readFile(fileName, (eror, data) => {
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

            // Get the array representing the wires
            let wire1 = [], wire2 = [];
            parseWire(rawWire[0], wire1);
            parseWire(rawWire[1], wire2);


            let distance = calculateMinDistance(wire1, wire2);
            if (distance != undefined)
            {
                console.log('Minimal distance between the two wires: ' + distance);
            }
        }
    });
}

function parseWire(raw, wire)
{
    let wireArray = raw.split(',');
    for (element in wireArray)
    {
        let steps = element.substr(1);
        wire.push({
            letter: element[0],
            steps: parseInt(steps, 10)
        })
    }
}

function calculateMinDistance(wire1, wire2)
{
    
}