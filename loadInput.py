from vehicle import Vehicle

currentStep = 0
score = 0
rides = []
popped = 0
meta = []

def initialize():
    global rides
    global meta
    f = open('easyS.txt')
    vehicles = []
    i = 0

    # get rides
    for line in f.readlines():
        if i == 0:
            meta = line.split()

        else:
            ride = line.split()
            rides.append(ride)
        i += 1
    j = 0

    # assign ride to vehicle
    for j in range(0, int(meta[2])):
        if (int(rides[0][7]) > 0):
            vehicle = Vehicle(0, 0, rides[0][0], rides[0][1], rides[0][2], rides[0][3], False, rides[0][4], j)
            vehicles.append(vehicle)
            rides.pop(0)
            global popped
            popped += 1
            print("popped: " + str(popped))
            print(rides[0])
        else:
            print("skip")
            rides.pop(0)
            print("popped: " + str(popped))
    for k in range(0, int(meta[5]) - 1):
        if len(rides) == 0:
            break
        else:
            step(vehicles)


def getNextRide(vehicle):
    global rides
    time = int(rides[0][5]) - currentStep
    xAfstandRit = abs(int(rides[0][2]) - int(rides[0][0]))
    xAfstandVehicleNaarRit = abs(int(rides[0][0]) - vehicle.position[0])
    yAfstandRit = abs(int(rides[0][3]) - int(rides[0][1]))
    yAfstandVehicleNaarRit = abs(int(rides[0][1]) - int(vehicle.position[1]))
    totaleAfstand = xAfstandRit + xAfstandVehicleNaarRit + yAfstandRit + yAfstandVehicleNaarRit

    # if we can make it on time
    if time > totaleAfstand:
        print("get new ride")
        vehicle = Vehicle(0, 0, rides[0][0], rides[0][1], rides[0][2], rides[0][3], False, rides[0][4], vehicle.index)
        rides.pop(0)
        global popped
        popped += 1
        print("popped: " + str(popped))
    #
    else:
        print("can't make it")
        return

def step(vehicles):
    global currentStep
    # let all vehicles make a step:
    for vehicle in vehicles:

        # move right
        if vehicle.xMovement > 0:
            vehicle.position[0] += 1
            vehicle.xMovement -= 1

        # move left
        elif vehicle.xMovement < 0:
            vehicle.position[0] -= 1
            vehicle.xMovement += 1

        # move up
        elif vehicle.yMovement > 0:
            vehicle.position[1] += 1
            vehicle.yMovement -= 1

        # move down
        elif vehicle.yMovement < 0:
            vehicle.position[1] -= 1
            vehicle.yMovement += 1

        # print ("xmovement: " + str(vehicle.xMovement))
        # print ("ymovement: " + str(vehicle.yMovement))

        if vehicle.xMovement == 0 and vehicle.yMovement == 0:
            global score
            # check if pick up or arrival
            if vehicle.hasBegun == False:
                # we have arrived at the passenger
                vehicle.hasBegun = True
                if (currentStep <= vehicle.earliest):
                    global meta
                    score += int(meta[4])
                vehicle.xMovement = int(vehicle.endRide[0]) - int(vehicle.position[0])
                vehicle.yMovement = int(vehicle.endRide[1]) - int(vehicle.position[1])

            # we have arrived at the destination of the passenger, add score
            else:
                vehicle.hasBegun = False
                #TODO ff chekcen of je wel score mag tellen
                score += abs(vehicle.beginRide[0] - vehicle.endRide[0]) + abs(vehicle.beginRide[1] - vehicle.endRide[1])
                # get next ride
                if len(rides) > 0:
                    getNextRide(vehicle)
                else:
                    return

    print(currentStep)
    currentStep += 1
    print(score)

initialize()
