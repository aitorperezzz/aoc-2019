import sys
import math

FILENAME = 'input.dat'
if len(sys.argv) == 2:
    FILENAME = sys.argv[1]

# Point class.
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = abs(self.x) + abs(self.y)

        # A point can have a minimal delay associated. None by default.
        self.steps = None

# Segment class (only vertical or horizontal segments).
class Segment():
    def __init__(self, initial, final):
        # First keep a copy of the initial and final points.
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

        # Keep a list of possible self-intersections for this segment.
        self.selfIntersections = []


# Receives a line of raw instructions and returns a list of segments.
def parseInstructions(raw):
    segments = []
    initialPoint = Point(0, 0)
    instructions = raw.split(',')

    # Fill in the segments according to each instruction.
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

        # Add the new segment given the initial and final points.
        segments.append(Segment(initialPoint, finalPoint))

        # Update the initial point.
        initialPoint = Point(finalPoint.x, finalPoint.y)

    return segments


# Gives the intersection between a horizontal and a vertical segment.
def simpleIntersection(horizontal, vertical):
    if horizontal.minx <= vertical.x and vertical.x <= horizontal.maxx:
            if vertical.miny <= horizontal.y and horizontal.y <= vertical.maxy:
                return Point(vertical.x, horizontal.y)

    return None


# Gets a possible array of points as the intersection of two segments.
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


# Gets an array of points and finds the closest to the origin.
def getClosest(intersection):
    best = Point(math.inf, math.inf)
    for point in intersection:
        if point.distance < best.distance:
            best = Point(point.x, point.y)
    return best


# For part one, find the distance to the closest intersection.
def closestIntersection(wire1, wire2):
    # Initially, the closest intersection point is infinity.
    closest = Point(math.inf, math.inf)

    # Traverse both lists of segments finding the closest intersection.
    for segment1 in wire1:
        for segment2 in wire2:
            intersection = getIntersection(segment1, segment2)
            if intersection:
                # In case the intersection is made up of several points, 
                # find the closest one.
                candidate = getClosest(intersection)
                if candidate.distance < closest.distance and candidate.x != 0 and candidate.y != 0:
                    closest = Point(candidate.x, candidate.y)

    return closest.distance

def getSteps(intersectionPoint, segment1, segment2):
    if segment1.initial.steps < segment2.initial.steps:

def parseSelfIntersections(wire):
    for segment in wire:
        for segmentAux in wire:
            if segment != segmentAux:
                # Get all self-intersections.
                intersection = getIntersection(segment, segmentAux)
                if intersection:
                    for point in intersection:
                        intersectionPoint = Point(point.x, point.y)
                        intersectionPoint.steps = getSteps(intersectionPoint, segment, segmentAux)
                else:


# For the second part, find the distance to the minimal delay intersection.
def minimalSignalDelay(wire1, wire2):
    intersections = []

    # Initially, the point with minimal delay is infinity.
    minimalDelayPoint = Point(math.inf, math.inf)
    minimalDelayPoint.minimalDelay = math.inf

    # Parse the self-intersections for each wire.
    parseSelfIntersections(wire1)
    parseSelfIntersections(wire2)

    # Traverse both lists of segments finding the point of minimal delay.
    for segment1 in wire1:
        for segment2 in wire2:
            intersection = getIntersection(segment1, segment2)
            if intersection:
                # In case the intersection is made up of several points, 
                # find the closest one.
                candidate = getClosest(intersection)
                if candidate.distance < closest.distance and candidate.x != 0 and candidate.y != 0:
                    closest = Point(candidate.x, candidate.y)

    return closest.distance


def solveProblem(fileName):
    # Open the input file.
    with open(fileName, 'r') as file:
        raw = file.readlines()

    # Parse both of the wire instructions into wire segments.
    wire1 = parseInstructions(raw[0].rstrip('\n'))
    wire2 = parseInstructions(raw[1].rstrip('\n'))

    # Calculate the intersection point with minimal distance.
    return closestIntersection(wire1, wire2)

result = solveProblem(FILENAME)
print('Distance to the closest intersection: ' + str(result))