class Vehicle:
    def __init__(self, x, y, beginX, beginY, endX, endY, hasBegun, earliest, index):
        self.position = [int(x), int(y)]
        self.xMovement = int(beginX) - int(x)
        self.yMovement = int(beginY) - int(y)
        self.beginRide = [int(beginX), int(beginY)]
        self.endRide = [int(endX), int(endY)]
        self.hasBegun = hasBegun
        self.earliest = int(earliest)
        self.index = index
    def __str__(self):
        output = "vehicle:\n"
        output += "current position: " + str(self.position) + "\n"
        output += "pick up passenger at: " + str(self.beginRide) + "\n"
        output += "bring him to: " + str(self.endRide) + "\n"
        return output
