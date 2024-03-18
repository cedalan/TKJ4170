import numpy as np
from get_radii import getRadii

radii = getRadii()
energies = open("energies.txt").read().split(",")
energies = [float(e) for e in energies]

min_energy = np.min(energies)

min_energy_index = np.where(energies == min_energy)[0][0]
print(min_energy_index)

print("Estimated equillibrium radii = " + str(radii[min_energy_index]))
print("Estimated equillibrium energy = " + str(min_energy))