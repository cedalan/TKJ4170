# Task 1 - CO:

In this task we want to do manual optimization of the geometry of C=O using restricted Hartree-Fock (RHF).

The automatic calculations are done in five (six) steps:

1. Specify which radii you want to RHF energy calculations on - You do this in create_radii_file.py.
2. Create file with these radii - Run create_radii_file.py after radii input.
3. Create readable files for NWCHem to read (and then calculate) - Run create_nw_files.py. It will automatically read from radii.txt
4. Run calculations - run calculations using run_calculations.py
5. Read energies - read energies using read_energies.py
6. Plot potential energy surface (PES) - run plot_PES.py