import os
def createFile(radius):
    myExamplefile = open("CO_example.txt", "r")

    try:
        folderPath = "CO_" + str(radius)
        os.mkdir(folderPath)
    except FileExistsError:
        pass

    #Replace this with the absolute path of your parent folder
    filePath = "/Users/elias/Documents/NTNU/V2024/TKJ4170/TKJ4170/Task2/Task 1 - CO/" + folderPath + "/CO_" + str(radius) + ".nw" 
    myFile = open(filePath, "w")

    for line in myExamplefile:
        if line.split() == []:
            myFile.write(line)
        elif line.split()[0] == "O":
            print("Line:" + line + "\n")

            words = line.split()
            words[3] = str(radius)

            line = " " +  " ".join(words)
            myFile.write(line + "\n")
        else:
            myFile.write(line)
    myFile.close()