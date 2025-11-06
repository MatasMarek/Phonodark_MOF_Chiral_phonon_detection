"""
    Material properties. For each atom in the primitive cell specify N, S, L, and L^i S^j
    values.

    Note: the order of the parameters must match the phonopy output. For a given material run phonopy
    once and examine the output to get this list

    date && python calculator.py -m inputs/material/mof/mof.py -p inputs/physics_model/light_dark_photon_born.py -n inputs/numerics/standard.py && date
"""
import numpy as np
import src.constants as const

material = "cdgform"

# number of atoms in the primitive cell
num_atoms = 46
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
			0.6553999244444444,  # H
			0.6553999244444444,  # H
			0.6553999244444444,  # H
			0.6553999244444444,  # H
			0.6553999244444444,  # H
			0.6553999244444444,  # H
			0.6553999244444444,  # H
			0.6553999244444444,  # H
			0.6553999244444444,  # H
			0.6553999244444444,  # H
			0.6553999244444444,  # H
			0.6553999244444444,  # H
			0.6553999244444444,  # H
			0.6553999244444444,  # H
			0.6553999244444444,  # H
			0.6553999244444444,  # H
			0.6553999244444444,  # H
			0.6553999244444444,  # H
			4.4079500991666665,  # C
			4.4079500991666665,  # C
			4.4079500991666665,  # C
			4.4079500991666665,  # C
			4.4079500991666665,  # C
			4.4079500991666665,  # C
			4.4079500991666665,  # C
			4.4079500991666665,  # C
			8.147032536666666,  # N
			8.147032536666666,  # N
			8.147032536666666,  # N
			8.147032536666666,  # N
			8.147032536666666,  # N
			8.147032536666666,  # N
			9.434487243333333,  # O
			9.434487243333333,  # O
			9.434487243333333,  # O
			9.434487243333333,  # O
			9.434487243333333,  # O
			9.434487243333333,  # O
			9.434487243333333,  # O
			9.434487243333333,  # O
			9.434487243333333,  # O
			9.434487243333333,  # O
			9.434487243333333,  # O
			9.434487243333333,  # O
			45.421362773333335,  # Cd
			45.421362773333335,  # Cd
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
			1,  # H
			1,  # H
			1,  # H
			1,  # H
			1,  # H
			1,  # H
			1,  # H
			1,  # H
			6,  # C
			6,  # C
			6,  # C
			6,  # C
			6,  # C
			6,  # C
			6,  # C
			6,  # C
			7,  # N
			7,  # N
			7,  # N
			7,  # N
			7,  # N
			7,  # N
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
			48,  # Cd
			48,  # Cd
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
			0.007940000000000058,  # H
			0.007940000000000058,  # H
			0.007940000000000058,  # H
			0.007940000000000058,  # H
			0.007940000000000058,  # H
			0.007940000000000058,  # H
			0.007940000000000058,  # H
			0.007940000000000058,  # H
			6.0107,  # C
			6.0107,  # C
			6.0107,  # C
			6.0107,  # C
			6.0107,  # C
			6.0107,  # C
			6.0107,  # C
			6.0107,  # C
			7.0067,  # N
			7.0067,  # N
			7.0067,  # N
			7.0067,  # N
			7.0067,  # N
			7.0067,  # N
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
			64.411,  # Cd
			64.411,  # Cd
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
