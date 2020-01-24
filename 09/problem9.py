import sys
sys.path.append('../')
import computer

if len(sys.argv) == 2:
    FILENAME = sys.argv[1]

program = computer.readProgramFromFile(FILENAME)
program.execute()
print(program.instructions)