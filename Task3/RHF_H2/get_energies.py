def getEnergies(radii):
    energies = []
    for radius in radii:
        print("Currently calculating energy for radius " + str(radius) + " Å")

        inputFile = open("H2_" + str(radius) + "/H2_" + str(radius) + ".out")

        for line in inputFile:
            if "Total SCF energy" in line:
                words = line.split()
                energies.append(words[-1])
    print(energies)
    return energies
