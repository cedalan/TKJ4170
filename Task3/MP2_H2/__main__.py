from create_nw_files_H2 import createNwFiles
from run_calculations import runCalculations
from get_energies import getEnergies
from save_radii_energies import saveRadiiEnergies
import matplotlib.pyplot as plt 

radii = [0.15 + 0.05 * i for i in range(20)]
while radii[-1] < 5:
    newradii = radii[-1] + 0.25
    radii.append(newradii)
createNwFiles(radii)
runCalculations(radii)
energies = getEnergies(radii)
energies = [float(e) for e in energies]

radii = [2 * r for r in radii] #THIS IS INCREDIBLY IMPORTANT TO REMEMBER!!!!!!!!!!!!!!!!!!!
#WE ARE USING SYMMETRY

saveRadiiEnergies(radii, energies, "MP2")

plt.plot(radii, energies, label="E(R)")
plt.title("$H_2$ dissociation curve,  MP2/aug-cc-pVDZ")
plt.xlabel("Radius (Å)")
plt.ylabel("Energy (Hartree)")
plt.grid()
plt.legend()
plt.savefig("H2_MP2.png")
plt.show()