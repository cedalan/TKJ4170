def main():
    from create_radii_file import createRadiiFile
    from create_nw_files import createNwFiles
    from get_radii import getRadii
    from run_calculations import runCalculations
    from create_energy_file import createEnergyFile

    if __name__ == "__main__":
        #Creates file from radii written in radii.txt
        createRadiiFile()

        #Gets radii from radii.txt
        radii = getRadii()
        print(radii)

        #Creates nw files from gotten radii
        createNwFiles(radii)

        #Runs energy calculations on the given radii
        runCalculations(radii)

        #Creates a file containing the energies of the radii
        createEnergyFile(radii)
main()