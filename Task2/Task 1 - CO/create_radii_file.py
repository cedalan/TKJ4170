def createRadiiFile():
    radiiFile = open("radii.txt", "w")

    radii = [0.75,0.80,0.85,0.90,0.95,1.0,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7, 1.8, 1.9, 2.0, 2.25, 2.5, 2.75, 3, 4, 5]

    for radius in radii:
        if radius != radii[-1]:
            radiiFile.write(str(radius) + ",")
        else:
            radiiFile.write(str(radius))

    radiiFile.close()
