import os

def runCalculations(radii):
    filesToRemove = ["molecule.cfock", "molecule.movecs"]
    for radius in radii:
        filePath = "H2_" + str(radius)
        inputFile = filePath + "/" + filePath + ".nw"
        outputFile = filePath + "/" + filePath + ".out"
        if os.path.exists(outputFile):
            print("Calculation has already been run for radius: " + str(radius))
            pass
        else:
            os.system("mpirun -np 4 nwchem " + inputFile +" > " + outputFile)
    
    for file in filesToRemove:
        os.system("rm " + file)
    