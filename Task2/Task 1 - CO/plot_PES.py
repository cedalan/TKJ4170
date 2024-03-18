import matplotlib.pyplot as plt 
import numpy as np
from get_radii import getRadii

radii = getRadii()
energies = open("energies.txt").read().split(",")
energies = [float(e) for e in energies]

print(radii)
print(energies)

plt.plot(radii, energies)
plt.show()
