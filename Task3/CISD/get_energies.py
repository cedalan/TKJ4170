def getEnergies(radii):
    energies = []
    for radius in radii:
        print("Fetching energy for radius = " + str(radius) + " Å")

        inputFile = open("H2_" + str(radius) + "/H2_" + str(radius) + ".out")

        for line in inputFile:
            if "CISD total energy / hartree" in line:
                words = line.split()
                energies.append(words[-1])
    return energies
