import sys
sys.path.append('../')
import computer
import math
import pdb

# Filename where the game is stored.
FILENAME = 'game.dat'

# Define the types of tiles.
TILE_EMPTY = 0
TILE_WALL = 1
TILE_BLOCK = 2
TILE_PADDLE = 3
TILE_BALL = 4

class Board():

    # Receives the first batch of outputs.
    def __init__(self, outputs):
        self.xsize = - math.inf
        self.ysize = - math.inf
        self.tiles = []
        self.score = None

        # Get the xsize and ysize of the board.
        for i in range(len(outputs)):
            if i % 3 == 0:
                # This is an x coordinate.
                if outputs[i] > self.xsize:
                    self.xsize = outputs[i]
            elif i % 3 == 1:
                # This is a y coordinate.
                if outputs[i] > self.ysize:
                    self.ysize = outputs[i]
        self.xsize += 1
        self.ysize += 1
        
        # Initialize the tiles.
        for i in range(self.ysize):
            self.tiles.append([])
            for j in range(self.xsize):
                self.tiles[i].append(TILE_EMPTY)
        
        # Decide how to print each of the tiles.
        self.characters = {
            TILE_EMPTY: ' ',
            TILE_WALL: '#',
            TILE_BLOCK: '+',
            TILE_PADDLE: '-',
            TILE_BALL: 'o'
        }

        # Store the positions of the ball and the paddle.
        self.ballx = 0
        self.paddlex = 0
    
    # Gets a new set of outputs and updates the values inside the board.
    def updateWithOutputs(self, outputs):
        position = 0
        while position < len(outputs):
            # Check if this is score information.
            if outputs[position] == -1 and outputs[position + 1] == 0:
                self.score = outputs[position + 2]
            
            # Check if this is tile information.
            if 0 <= outputs[position] and outputs[position] < self.xsize:
                x = outputs[position]
                if 0 <= outputs[position + 1] and outputs[position + 1] < self.ysize:
                    y = outputs[position + 1]
                    self.tiles[y][x] = outputs[position + 2]
            
            # Check if this was the ball and store its position.
            if outputs[position + 2] == TILE_BALL:
                self.ballx = outputs[position]
            
            # Check if this was the paddle and store its position.
            if outputs[position + 2] == TILE_PADDLE:
                self.paddlex = outputs[position]
            
            position += 3
    
    def decideNextJoystickMovement(self):
        diff = self.ballx - self.paddlex
        return diff / abs(diff) if diff != 0 else 0
    
    # Prints the information about this board.
    def print(self):

        # Print the score.
        print('Score: {}'.format(self.score))

        # Print the tiles.
        for y in range(self.ysize):
            for x in range(self.xsize):
                print(self.characters[self.tiles[y][x]], end='')
            print()
        print()

def main(filename):

    # Load instructions from the file.
    gameInstructions = computer.readInstructionsFromFile(filename)
    
    # Solve part one of the problem.
    count = numberOfBlockTiles(gameInstructions)
    print('Number of block tiles: {}'.format(count))

    # Solve part two of the problem playing the game.
    score = playGame(gameInstructions)
    print('Score after winning: {}'.format(score))


# Loads the game and counts the number of block tiles.
def numberOfBlockTiles(instructions):

    # Load the game and execute it.
    game = computer.Program(instructions)
    game.printOutputs(False)
    game.execute()
    outputs = game.getOutputs()

    # Count the number of block tiles.
    blocks = 0
    for i in range(len(outputs)):
        if i % 3 == 2 and outputs[i] == 2:
            blocks += 1
    
    return blocks

# Plays the game and returns the score after winning.
def playGame(instructions):

    # Load the game.
    game = computer.Program(instructions)
    game.setMemory(0, 2)
    game.printOutputs(False)

    # Define a board.
    board = None

    while True:

        # Execute the next turn of the game.
        game.pauseBeforeInputInstruction(True)
        result = game.execute()

        # Get the outputs and initialize the board if needed.
        outputs = game.getOutputs()
        if board == None:
            board = Board(outputs)
        
        # Update the tiles and the score.
        board.updateWithOutputs(outputs)

        # Exit if the game halted.
        if result == computer.FINISH_HALT:
            break

        # Decide where to move the joystick.
        game.setInputs([board.decideNextJoystickMovement()])
        
        # Execute the joystick input instruction.
        game.executeInputAfterPause()

    return board.score

if __name__ == '__main__':
    main(FILENAME)
