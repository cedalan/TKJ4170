def createRadiiFile():
    radiiFile = open("radii.txt", "w")

    radii = [0.75,0.85,0.95,1.0,1.10,1.20,1.30,1.40,1.50,1.60,1.70]

    for radius in radii:
        if radius != radii[-1]:
            radiiFile.write(str(radius) + ",")
        else:
            radiiFile.write(str(radius))

    radiiFile.close()
