def getRadii():
    radiiFile = open("radii.txt", "r")
    line = radiiFile.readline()
    radiiFile.close()

    radii = line.split(",")
    radii = [float(radius) for radius in radii]
    return radii