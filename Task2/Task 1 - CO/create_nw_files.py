import os
def createNwFiles(radii):
    myExampleFile = open("CO_example.txt", "r")

    for radius in radii:
        try:
            folderPath = "CO_" + str(radius)
            os.mkdir(folderPath)
        except FileExistsError:
            print("Path already exists, or does it?")
            pass

        filePath = "/Users/elias/Documents/NTNU/V2024/TKJ4170/TKJ4170/Task2/Task 1 - CO/" + folderPath + "/CO_" + str(radius) + ".nw"
        myFile = open(filePath, "w")

        for line in myExampleFile:
            if line.split() == []:
                myFile.write(line)
            elif line.split()[0] == "O":

                words = line.split()
                words[3] = str(radius)

                line = " " +  " ".join(words)
                myFile.write(line + "\n")
            else:
                myFile.write(line)
        myFile.close()
    myExampleFile.close()
        
