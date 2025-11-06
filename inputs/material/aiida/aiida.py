"""
    Material properties. For each atom in the primitive cell specify N, S, L, and L^i S^j
    values.

    Note: the order of the parameters must match the phonopy output. For a given material run phonopy
    once and examine the output to get this list

    TODO: automate this process, specify values for unique atoms in cell and fill these vectors with the
    appropriate values.
    # date && python calculator.py -m inputs/material/aiida/aiida.py -p inputs/physics_model/light_dark_photon_born.py -n inputs/numerics/standard.py && date
"""
import numpy as np
import src.constants as const

material = 'aiida'

# number of atoms in the primitive cell
num_atoms = 36
# num_atoms = 5
mat_properties_dict = {
        # dimension of supercell used in DFT calculation
        "supercell_dim": [1., 1., 1.],
	"mass":{
		"e": const.M_ELEC,
		"p": const.M_NUCL,
		"n": const.M_NUCL
	},
	"N_list": {
		"e": np.array([
			13.0 - 3.0,  # TODO: find how many electrons to add where;  2*-3 + 2*1 + 8*0.5 + 16*0 + 8*0 = 4!
			9.0 + 1,  # F
			8.0 + 0.5,  # O
			6.0,  # C
			1.0  # H
		]),
		"p": np.array([
			13.0,  # Al
			9.0,  # F
			8.0,  # O
			6.0,  # C
			1.0  # H
		]),
		"n": np.array([
			26.982 - 13.0,  # Al
			18.99 - 9.0,  # F
			15.99 - 8.0,  # O
			12.01 - 6.0,  # C
			1.0 - 1.0  # H
		])
	},
	"L_S_list": {
		"e": np.zeros(num_atoms),
		"p": np.zeros(num_atoms),
		"n": np.zeros(num_atoms)
	},
	"S_list": {
		"e": np.zeros((num_atoms, 3)),
		"p": np.zeros((num_atoms, 3)),
		"n": np.zeros((num_atoms, 3))
	},
	"L_list": {
		"e": np.zeros((num_atoms, 3)),
		"p": np.zeros((num_atoms, 3)),
		"n": np.zeros((num_atoms, 3))
	},
	"L_tens_S_list": {
		"e": np.zeros((num_atoms, 3, 3)),
		"p": np.zeros((num_atoms, 3, 3)),
		"n": np.zeros((num_atoms, 3, 3))
	},
}
