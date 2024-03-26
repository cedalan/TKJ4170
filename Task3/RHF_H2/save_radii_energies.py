def saveRadiiEnergies(radii, energies, method):
    energyFile = open("radii_and_energies_H2_" + method + ".txt", "w")

    for r, e in zip(radii, energies):
        energyFile.write(str(r) + "," + str(e) + "\n")

    energyFile.close()