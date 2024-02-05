radii = [1.0, 1.25, 1.5, 1.75, 2.0]
            

def createFileEasy(radius):
    myExamplefile = open("/Users/elias/Documents/NTNU/V2024/TKJ4170/Oving2/Task 1 - CO/CO_example.txt", "r")
    myFile = open("C0_" + str(radius) + ".nw", "w")

    for line in myExamplefile:
        if line.split() == []:
            myFile.write(line)
        elif line.split()[0] == "O":
            print("Line:" + line + "\n")

            words = line.split()
            words[3] = str(radius)

            print("Old line: " + line + "\n")
            line = " " +  " ".join(words)
            myFile.write(line + "\n")
        else:
            myFile.write(line)
    myFile.close()


createFileEasy(0.10)