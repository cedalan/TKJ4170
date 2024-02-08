import os

def runCalculations(radii):
    filesToRemove = ["molecule.b", "molecule.b^-1", "molecule.c", "molecule.cfock", "molecule.db", "molecule.movecs", "molecule.p", "molecule.zmat"]
    for radius in radii:
        filePath = "CO_" + str(radius)
        inputFile = filePath + "/" + filePath + ".nw"
        outputFile = filePath + "/" + filePath + ".out"
        os.system("mpirun -np 4 nwchem " + inputFile +" > " + outputFile)
    
    for file in filesToRemove:
        os.system("rm " + file)
    for radius in radii:
        os.system("rm " + "CO_" + str(radius) + ".db")