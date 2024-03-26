import os
def createNwFiles(radii):
    for radius in radii:
        print("Running for radius = " + str(radius) + " Å")
        try:
            folderPath = "H2_" + str(radius)
            os.mkdir(folderPath)
        except FileExistsError:
            print("Folder already exists for radius = " + str(2 * radius) + " Å")

        filePath = "/Users/elias/Documents/NTNU/V2024/TKJ4170/TKJ4170/Task3/RHF_H2/" + folderPath + "/H2_" + str(radius) + ".nw"
        myExampleFile = open("H2.nw", "r")

        with open(filePath, "w") as myFile:
            for line in myExampleFile:
                if line.split() == []:
                    myFile.write(line)
                elif "rad" in line:
                    line = line.split(" ")
                    line = [word.replace("rad", str(radius)) for word in line]
                    line = " ".join(line)
                    myFile.write(line)
                else:
                    myFile.write(line)

        myExampleFile.close()
        print("Successful creation for radius = " + str(2 * radius) + " Å \n")