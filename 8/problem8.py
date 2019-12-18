# Decide the name of the file.
FILENAME = 'image.dat'

# Declaration for the layer class.
class Layer():
    def __init__(self):
        # Double array containing all the pixels of the layer.
        self.pixels =[]
        # Dictionary containing the info about the count of each digit.
        self.count = {}

# Prints the message in an image in the form of layers.
def printMessage(layers):
    print('Message inside the image:')
    for i in range(0, 6):
        for j in range(0, 25):
            # Search for the first non-transparent pixel.
            for layer in layers:
                if layer.pixels[i][j] == '0':
                    print('#', end='')
                    break
                elif layer.pixels[i][j] == '1':
                    print(' ', end='')
                    break

        # After completing a line, print a newline.
        print()
    print()

def solveProblem(fileName):
    # Load the image from the file as a string.
    with open(fileName, 'r') as file:
        image = file.read()

    # Create a list with the information for each layer.
    layers = []

    # Parse the image information.
    layer = 0
    best = layer
    position = 0
    while position < len(image):
        # Add a new layer to the list.
        layers.append(Layer())

        for i in range(0, 6):
            # Start a new row.
            layers[layer].pixels.append([])

            for j in range(0, 25):
                # Keep the info about this pixel.
                layers[layer].pixels[i].append(image[position])

                # Update the total count of pixels.
                if image[position] in layers[layer].count:
                    layers[layer].count[image[position]] += 1
                else:
                    layers[layer].count[image[position]] = 1

                # Update the global position.
                position += 1

        # Find the number of zeros of this layer just created and update if necessary.
        if layers[layer].count['0'] < layers[best].count['0']:
            best = layer

        # Update the number of layers.
        layer += 1

    # Print out the message inside the image.
    printMessage(layers)

    # Return the sum of 1 and 2 digits in the best layer.
    return layers[best].count['1'] * layers[best].count['2']


result = solveProblem(FILENAME)     
print('Number of 1 and 2 digits in the best layer: {}'.format(result))

