from math import *

def coordsDict(file):
    coordsDict = {}

    ballList = []
    for f in file.readlines():
        if f[:11] == 'sports ball':
            ballList.append(f.split())
        elif f[:6] == 'person':
            personList = f.split()

    leftx0 = int(ballList[0][4])
    topy0 = int(ballList[0][6])
    width0 = int(ballList[0][8])
    height0 = int(ballList[0][10][:-1])

    leftx1 = int(ballList[1][4])
    topy1 = int(ballList[1][6])
    width1 = int(ballList[1][8])
    height1 = int(ballList[1][10][:-1])

    topy = int(personList[5])
    height = int(personList[9][:-1])

    ground = height + topy
    
    coordsDict['centerx0'] = leftx0 + (width0>>1)
    coordsDict['centery0'] = topy0 + (height0>>1)

    coordsDict['centerx1'] = leftx1 + (width1>>1)
    coordsDict['centery1'] = topy1 + (height1>>1)

    coordsDict['ground'] = ground

    coordsDict['minSize'] = min(width0, height0)

    return coordsDict

def getAngle(x0, y0, x1, y1):

    xdiff = x1 - x0
    ydiff = y0 - y1

    angle = atan(ydiff/xdiff)

    print ("angle = ", angle)

    return angle

def getBallHeight(ground, ballHeight, ballSize):

    height = ground - ballHeight
    height = (height * 0.21)/ballSize

    print("height = ", height)

    return height

def getVelocity(x0, y0, x1, y1, ballSize, timeDiff):

    xdiff = x1 - x0
    ydiff = y0 - y1

    v = sqrt(xdiff**2 + ydiff**2)
    v = (v * 0.21)/ballSize
    v = v/timeDiff

    print("velocity = ", v)

    return v

def getDist(v, angle, height):

    g = 9.8
    dist = v*cos(angle)*(v*sin(angle)+sqrt((v*sin(angle))**2+2*g*height))/g

    print("distance = ", dist)

    return dist

def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == "-":
            opts[argv[0]] = argv[1]
            argv = argv[2:]
        else:
            argv = argv[1:]
    return opts

if __name__ == '__main__':
    from sys import(argv)
    myargs = getopts(argv)
    if '-file' in myargs:
        fileName = myargs['-file']
    else:
        print('insert results file')
        exit

    if '-interval' in myargs:
        timeDiff = float(myargs['-interval'])
    else:
        print('error: no time diff')
        exit
    
    file = open(fileName)

    coordsDict = coordsDict(file)
    angle = getAngle(coordsDict['centerx0'], coordsDict['centery0'], coordsDict['centerx1'], coordsDict['centery1'])
    height = getBallHeight(coordsDict['ground'], coordsDict['centery0'], coordsDict['minSize'])
    velocity = getVelocity(coordsDict['centerx0'], coordsDict['centery0'], coordsDict['centerx1'], coordsDict['centery1'], coordsDict['minSize'], timeDiff)
    dist = getDist(velocity, angle, height)

    print("ball traveled ", dist, " meters")
    



