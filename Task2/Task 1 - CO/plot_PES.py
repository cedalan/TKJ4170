import matplotlib.pyplot as plt 
import numpy as np
from get_radii import getRadii

radii = getRadii()
energies = open("energies.txt").read().split(",")
energies = [float(e) for e in energies]

print(radii)
print(energies)

newRadii = []
newEnergies = []

for r, e in zip(radii, energies):
    if (r > 2):
        break 
    else:
        newRadii.append(r)
        newEnergies.append(e)

minR = newRadii[newEnergies.index(min(newEnergies))]
minE = min(newEnergies)


plt.scatter([minR], [minE], label="Lowest point of energy", color="red", zorder=100)
plt.plot(newRadii, newEnergies, label="E(R)")
plt.annotate(f"({minR},{round(minE, 3)})", xy=(minR - 0.1, minE + 0.05))
plt.title("$CO$ potential energy surface,  RHF/cc-pVDZ")
plt.xlabel("Radius (Å)")
plt.ylabel("Energy (Hartree)")
plt.grid()
plt.legend()
plt.savefig("CO_PES.png")
plt.show()