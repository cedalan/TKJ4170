def createEnergyFile(radii):
    energies = []

    for radius in radii:
        print("Currently calculating energy for radius " + str(radius) + " Å")
        print("Energies collected are: ")
        for energy in energies:
            print(energy)
        dummyEnergies = []
        inputFile = open("CO_" + str(radius) + "/CO_" + str(radius) + ".out")
        
        energyFound = False

        for line in inputFile:
            words = line.split()

            if energyFound:
                if len(line) == 1:
                    break
                if words[0].isdigit():
                    dummyEnergies.append(float(words[1]))
                elif "-" in words[0]:
                    pass

            if "iter" in words:
                energyFound = True
        energies.append(str(dummyEnergies[-1]))
        inputFile.close()

    energyFile = open("energies.txt", "w")
    for energy in energies:
        if energy != energies[-1]:
            energyFile.write(energy + ",")
        else:
            energyFile.write(energy)
    energyFile.close()

    return radii, energies