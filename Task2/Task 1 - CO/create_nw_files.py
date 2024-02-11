import os
def createNwFiles(radii):
    for radius in radii:
        print("Running for radius = " + str(radius) + " Å")
        try:
            folderPath = "CO_" + str(radius)
            os.mkdir(folderPath)
        except FileExistsError:
            print("Folder already exists for radius = " + str(radius) + " Å")

        filePath = "/Users/elias/Documents/NTNU/V2024/TKJ4170/TKJ4170/Task2/Task 1 - CO/" + folderPath + "/CO_" + str(radius) + ".nw"
        myExampleFile = open("CO_example.txt", "r")

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
        print("Successful creation for radius = " + str(radius) + " Å \n")