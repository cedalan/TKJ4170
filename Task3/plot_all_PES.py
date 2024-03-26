import numpy as np 
import matplotlib.pyplot as plt 

data_RHF = np.loadtxt("RHF_H2/radii_and_energies_H2_RHF.txt", delimiter=",")
data_MP2 = np.loadtxt("MP2_H2/radii_and_energies_H2_MP2.txt", delimiter=",")
data_CISD = np.loadtxt("CISD/radii_and_energies_H2_CISD.txt", delimiter=",")

radii_RHF = data_RHF[:,0]
radii_MP2 = data_MP2[:,0]
radii_CISD = data_CISD[:,0]

energies_RHF = data_RHF[:,1]
energies_MP2 = data_MP2[:,1]
energies_CISD = data_CISD[:,1]

plt.plot(radii_RHF, energies_RHF, label="$E_{RHF}(R)$")
plt.plot(radii_MP2, energies_MP2, label="$E_{MP2}(R)$")
plt.plot(radii_CISD, energies_CISD, label="$E_{CISD}(R)$")
plt.title("$H_2$ dissociation curves - basis: aug-cc-pVDZ")
plt.xlabel("Radius (Å)")
plt.ylabel("Energy (Hartree)")
plt.grid()
plt.legend()
plt.savefig("all_PES.png")
plt.show()

print(f"RHF $H_2$ dissociation energy: {energies_RHF[-1]}")
print(f"CISD $H_2$ dissociation energy: {energies_CISD[-1]}")