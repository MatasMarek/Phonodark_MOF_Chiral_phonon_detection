"""
    Material properties. For each atom in the primitive cell specify N, S, L, and L^i S^j
    values.

    Note: the order of the parameters must match the phonopy output. For a given material run phonopy
    once and examine the output to get this list

    date && python calculator.py -m inputs/material/mof/mof.py -p inputs/physics_model/light_dark_photon_born.py -n inputs/numerics/standard.py && date
"""
import numpy as np
import src.constants as const

material = "litar"

# number of atoms in the primitive cell
num_atoms = 32
mat_properties_dict = {
        # dimension of supercell used in DFT calculation
"supercell_dim": [1.0, 1.0, 1.0],
	"mass":{
		"e": const.M_ELEC,
		"p": const.M_NUCL,
		"n": const.M_NUCL
	},
	"N_list": {
		"e": np.array([
			0.559272212,  # H
			0.559272212,  # H
			0.559272212,  # H
			0.559272212,  # H
			0.559272212,  # H
			0.559272212,  # H
			0.559272212,  # H
			0.559272212,  # H
			0.559272212,  # H
			0.559272212,  # H
			1.8605020566666666,  # Li
			1.8605020566666666,  # Li
			5.060181083333333,  # C
			5.060181083333333,  # C
			5.060181083333333,  # C
			5.060181083333333,  # C
			5.060181083333333,  # C
			5.060181083333333,  # C
			5.060181083333333,  # C
			5.060181083333333,  # C
			9.18370221,  # O
			9.18370221,  # O
			9.18370221,  # O
			9.18370221,  # O
			9.18370221,  # O
			9.18370221,  # O
			9.18370221,  # O
			9.18370221,  # O
			9.18370221,  # O
			9.18370221,  # O
			9.18370221,  # O
			9.18370221,  # O
		]),
		"p": np.array([
			1,  # H
			1,  # H
			1,  # H
			1,  # H
			1,  # H
			1,  # H
			1,  # H
			1,  # H
			1,  # H
			1,  # H
			3,  # Li
			3,  # Li
			6,  # C
			6,  # C
			6,  # C
			6,  # C
			6,  # C
			6,  # C
			6,  # C
			6,  # C
			8,  # O
			8,  # O
			8,  # O
			8,  # O
			8,  # O
			8,  # O
			8,  # O
			8,  # O
			8,  # O
			8,  # O
			8,  # O
			8,  # O
		]),
		"n": np.array([
			0.007940000000000058,  # H
			0.007940000000000058,  # H
			0.007940000000000058,  # H
			0.007940000000000058,  # H
			0.007940000000000058,  # H
			0.007940000000000058,  # H
			0.007940000000000058,  # H
			0.007940000000000058,  # H
			0.007940000000000058,  # H
			0.007940000000000058,  # H
			3.941,  # Li
			3.941,  # Li
			6.0107,  # C
			6.0107,  # C
			6.0107,  # C
			6.0107,  # C
			6.0107,  # C
			6.0107,  # C
			6.0107,  # C
			6.0107,  # C
			7.9994,  # O
			7.9994,  # O
			7.9994,  # O
			7.9994,  # O
			7.9994,  # O
			7.9994,  # O
			7.9994,  # O
			7.9994,  # O
			7.9994,  # O
			7.9994,  # O
			7.9994,  # O
			7.9994,  # O
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
