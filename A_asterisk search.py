import math
class Location:
    nameOfLocation = ""
    x_pos = 0
    y_pos = 0
    def __init__(self,nameOfLocation,co_ordinates):
        self.nameOfLocation = nameOfLocation
        self.x_pos = co_ordinates[0]
        self.y_pos = co_ordinates[1]
    def connectedTo(self,connectedTo):
        self.connectedTo = connectedTo

A = Location("A",[0,0])
B = Location("B",[1,2])
C = Location("C",[1,0])
D = Location("D",[1,-1])
E = Location("E",[2,1.4])
F = Location("F",[2,1])
G = Location("G",[3,0])
H = Location("H",[3,1.4])
I = Location("I",[4.6,0.4])
J = Location("J",[4,-1])

A.connectedTo([B,C,D])
B.connectedTo([A,E])
C.connectedTo([A,F,G])
D.connectedTo([A,J])
E.connectedTo([B,F,H])
F.connectedTo([E,C,G])
G.connectedTo([F,C,I])
H.connectedTo([E,I])
I.connectedTo([H,G,J])
J.connectedTo([D,I])

def getHeuresticsDistance(startingPoint,endPoint):
     return math.sqrt(math.pow(endPoint.x_pos-startingPoint.x_pos,2)+ math.pow(endPoint.y_pos-startingPoint.y_pos,2))
def my_min(sequence):
    low = sequence[0] # need to start with some value
    for i in sequence:
        if i < low:
            low = i
    return low
def findPathTo(startingPoint, endPoint):
    locationsTravelled = []
    hasReachedEndOfLoop = False
    locationsTravelled.append(startingPoint.nameOfLocation)

    while not hasReachedEndOfLoop:
        h_array = []
        for i in startingPoint.connectedTo:
            h_array.append(getHeuresticsDistance(i,endPoint)+getHeuresticsDistance(startingPoint,i))
        pos = h_array.index(my_min(h_array))

        if (startingPoint.nameOfLocation == endPoint.nameOfLocation):
            hasReachedEndOfLoop = True
            return (locationsTravelled)
        else:
            startingPoint = startingPoint.connectedTo[pos]
            locationsTravelled.append(startingPoint.nameOfLocation)

print(findPathTo(A,I))