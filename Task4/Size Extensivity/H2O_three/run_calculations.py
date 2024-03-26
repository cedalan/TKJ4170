import numpy as np 
import os 

mp2 = "task mp2"
rhf = "task scf"
cisd = "tce\n cisd \nend \n\ntask tce energy"
ccsd = "tce\n ccsd \nend \n\ntask tce energy"

methods = [mp2, rhf, cisd, ccsd]
methodNames = ["MP2", "RHF", "CISD", "CCSD"]

def createFiles(methods, methodnames):
    for method, name in zip(methods, methodNames):
        exampleFile = open("H2O_three.nw", "r")
        methodFile = open("H2O_three_" + name + ".nw", "w")

        for line in exampleFile:
            if (line != "task mp2"):
                methodFile.write(line)
            else:
                methodFile.write(method)
        
        methodFile.close()

def doCalculations(methods):
    for method in methods:
        inputFile = "H2O_three_" + method + ".nw"
        outputFile = "H2O_three_" + method + ".out"
        if os.path.exists(outputFile):
            print("Calculation has already been run for method: " + method)
            pass
        else:
            os.system("mpirun -np 4 nwchem " + inputFile + " > " + outputFile)

    filesToRemove = ["molecule.b", "molecule.c", "molecule.b^-1", "molecule.c", "molecule.cfock", "molecule.db", "molecule.movecs", "molcule.p", "molecule.zmat"]
    for fileToRemove in filesToRemove:
        os.system("rm " + fileToRemove)

createFiles(methods, methodNames)
doCalculations(methodNames)