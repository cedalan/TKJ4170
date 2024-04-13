import numpy as np 
import os 

mp2 = "task mp2"
rhf = "task scf"
cisd = "tce\n cisd \nend \n\ntask tce energy"
ccsd = "tce\n ccsd \nend \n\ntask tce energy"

methodCalls = [mp2, rhf, cisd, ccsd]
methodNames = ["MP2", "RHF", "CISD", "CCSD"]
basisSets = ["cc-PVDZ", "cc-PVTZ", "aug-cc-PVDZ", "aug-cc-PVTZ"]

def createFiles(method_calls, method_names, basis_sets):
    for basis_set in basis_sets:
        print("Creating file(s) for basis set: " + basis_set)
        try:
            folderPath = basis_set
            os.mkdir(folderPath)
        except FileExistsError:
            print("Some, or all calculations have already been done for this basis set")
        
        for method_call, method_name in zip(method_calls, method_names):
            print("Creating file for method: " + method_name)
            filePath = "/Users/elias/Documents/NTNU/V2024/TKJ4170/TKJ4170/Task4/Correlation energy/" + basis_set + "/" + method_name
            #TODO: Create new nw files for method


            myExampleFile = open("formaldehydeOptimized.nw", "r")

            with open(filePath + ".nw", "w") as myFile:
                for line in myExampleFile:
                    print(line)
                    if (line == "poop pee\n"):
                        print("Does this even run once?")
                        myFile.write("* library " + basis_set + "\n")
                    elif (line == "task scf"):
                        myFile.write(method_call)
                    else:
                        myFile.write(line)
            myExampleFile.close()
            print("Done creating file for method: " + method_name + "\n")

        print("Done creating file(s) for basis set: " + basis_set + "\n")

def runCalculations(method_names, basis_sets):
    filesToRemove = ["molecule.b", "molecule.b^-1", "molecule.c", "molecule.cfock", "molecule.db", "molecule.movecs", "molecule.p", "molecule.zmat", "CCSD.db", "CISD.db", "RHF.db"]

    for basis_set in basis_sets:
        print("Running calculation(s) for basis set: " + basis_set)

        for method_name in method_names:
            print("Running calculation for method: " + method_name)

            filePath = basis_set + "/" + method_name
            inputFile = filePath + ".nw"
            outputFile = filePath + ".out"

            os.system("mpirun -np 4 nwchem " + inputFile + " > " + outputFile)

            for file in filesToRemove:
                os.system("rm " + file)

            print("Done running calculation for method: " + method_name)

        print("Done running calculation(s) for basis set: " + basis_set + "\n")

createFiles(methodCalls, methodNames, basisSets)
runCalculations(methodNames, basisSets)