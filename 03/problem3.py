import sys
import math

# Choose a name for the input file.
FILENAME = 'input.dat'
if len(sys.argv) == 2:
    FILENAME = sys.argv[1]

# Point class.
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # Calculate Manhattan distance to the origin.
        self.distance = abs(self.x) + abs(self.y)

        # A point can have a minimal signal delay associated.
        self.minimalSignalDelay = None

# Segment class (vertical or horizontal segments).
class Segment():
    def __init__(self, initial, final):

        # Keep a copy of the initial and final points.
        self.initial = Point(initial.x, initial.y)
        self.final = Point(final.x, final.y)

        if initial.x == final.x:
            # Vertical segment.
            self.type = 'ver'
            self.x = initial.x
            self.miny = min(initial.y, final.y)
            self.maxy = max(initial.y, final.y)
        else:
            # Horizontal segment.
            self.type = 'hor'
            self.y = initial.y
            self.minx = min(initial.x, final.x)
            self.maxx = max(initial.x, final.x)

        # Keep the acumulated steps until this segment.
        self.steps = 0


# Receives a line of raw instructions and returns a list of segments.
def parseInstructions(raw):
    segments = []
    initialPoint = Point(0, 0)
    instructions = raw.split(',')

    # Fill in the segments according to each instruction.
    totalSteps = 0
    for instruction in instructions:
        step = int(instruction[1:])

        # Find out the final point for the segment.
        if instruction[0] == 'U':
            finalPoint = Point(initialPoint.x, initialPoint.y + step)
        elif instruction[0] == 'D':
            finalPoint = Point(initialPoint.x, initialPoint.y - step)
        elif instruction[0] == 'R':
            finalPoint = Point(initialPoint.x + step, initialPoint.y)
        elif instruction[0] == 'L':
            finalPoint = Point(initialPoint.x - step, initialPoint.y)

        # Create a new segment and add it to the list.
        segment = Segment(initialPoint, finalPoint)
        segment.steps = totalSteps
        segments.append(segment)

        # Update the initial point and the total of steps.
        initialPoint = Point(finalPoint.x, finalPoint.y)
        totalSteps += step

    return segments


# Gives the intersection between a horizontal and a vertical segment.
def simpleIntersection(horizontal, vertical):
    if horizontal.minx <= vertical.x and vertical.x <= horizontal.maxx:
            if vertical.miny <= horizontal.y and horizontal.y <= vertical.maxy:
                return Point(vertical.x, horizontal.y)

    return None


# Gets all the points in the intersection between two segments.
def getIntersection(segment1, segment2):
    intersection = []

    # Both are horizontal.
    if segment1.type == segment2.type == 'hor':
        if segment1.y == segment2.y:
            for i in range(max(segment1.minx, segment2.minx), min(segment1.maxx, segment2.maxx) + 1):
                intersection.append(Point(i, segment1.y))
    # Both are vertical.
    elif segment1.type == segment2.type == 'ver':
        if segment1.x == segment2.x:
            for i in range(max(segment1.miny, segment2.miny), min(segment1.maxy, segment2.maxy)):
                intersection.append(Point(segment1.x, i))
    # Each one is a different type.
    elif segment1.type == 'hor':
        simple = simpleIntersection(segment1, segment2)
        if simple != None:
            intersection.append(simple)
    elif segment1.type == 'ver':
        simple = simpleIntersection(segment2, segment1)
        if simple != None:
            intersection.append(simple)
    
    # Return the list (if no point found, the list is empty).
    return intersection


# Receives a list of points and finds the closest to the origin.
def getClosest(points):
    best = Point(math.inf, math.inf)
    for point in points:
        if point.distance < best.distance:
            best = Point(point.x, point.y)
    return best


# Receives a point inside a segment and calculates the partial signal delay.
def getPartialDelay(point, segment):
    if segment.type == 'hor':
        return abs(point.x - segment.initial.x)
    else:
        return abs(point.y - segment.initial.y)

def updateMinimalDelayInfo(point, segment1, segment2):
    partialDelay1 = getPartialDelay(point, segment1)
    partialDelay2 = getPartialDelay(point, segment2)

    point.minimalSignalDelay = segment1.steps + segment2.steps + partialDelay1 + partialDelay2

# Find the minimal distance to an intersection, and also
# the minimal signal delay to an intersection.
def findMinimalValues(wire1, wire2):

    # Initial minimal points are at infinity.
    closestPoint = Point(math.inf, math.inf)
    minimalDelayPoint = Point(math.inf, math.inf)
    minimalDelayPoint.minimalSignalDelay = math.inf

    # Traverse all combinations of segments.
    for segment1 in wire1:
        for segment2 in wire2:

            # Get the complete intersection between the segments.
            intersection = getIntersection(segment1, segment2)

            if intersection:
                # Find the closest point in the intersection as a candidate.
                candidate = getClosest(intersection)

                # Update the best if needed.
                if candidate.distance < closestPoint.distance and candidate.x != 0 and candidate.y != 0:
                    closestPoint = Point(candidate.x, candidate.y)
                
                # For minimal signal delay, go through all points in the intersection.
                for point in intersection:

                    # Get the minimal delay value for this point.
                    updateMinimalDelayInfo(point, segment1, segment2)

                    # Update the best if needed.
                    if point.minimalSignalDelay < minimalDelayPoint.minimalSignalDelay and point.x != 0 and point.y != 0:
                        minimalDelayPoint = Point(point.x, point.y)
                        minimalDelayPoint.minimalSignalDelay = point.minimalSignalDelay


    return {'closest':closestPoint.distance,'minDelay':minimalDelayPoint.minimalSignalDelay}


def solveProblem(fileName):
    # Open the input file.
    with open(fileName, 'r') as file:
        raw = file.readlines()

    # Parse both of the wire instructions into wire segments.
    wire1 = parseInstructions(raw[0].rstrip('\n'))
    wire2 = parseInstructions(raw[1].rstrip('\n'))

    # Calculate the values for dat 3.
    return findMinimalValues(wire1, wire2)

result = solveProblem(FILENAME)
print('Distance to the closest intersection: ' + str(result['closest']))
print('Minimal signal delay: ' + str(result['minDelay']))