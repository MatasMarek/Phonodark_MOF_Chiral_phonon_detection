"""
    Material properties. For each atom in the primitive cell specify N, S, L, and L^i S^j
    values.

    Note: the order of the parameters must match the phonopy output. For a given material run phonopy
    once and examine the output to get this list

    date && python calculator.py -m inputs/material/mof/mof.py -p inputs/physics_model/light_dark_photon_born.py -n inputs/numerics/standard.py && date
"""
import numpy as np
import src.constants as const

material = "linbo3"

# number of atoms in the primitive cell
num_atoms = 1250
mat_properties_dict = {
        # dimension of supercell used in DFT calculation
"supercell_dim": [5.0, 5.0, 5.0],
	"mass":{
		"e": const.M_ELEC,
		"p": const.M_NUCL,
		"n": const.M_NUCL
	},
	"N_list": {
		"e": np.array([
			10.74466946,  # O
			10.74466946,  # O
			10.74466946,  # O
			10.74466946,  # O
			10.74466946,  # O
			10.74466946,  # O
			33.910366126666666,  # Nb
			33.910366126666666,  # Nb
			1.8550455866666669,  # Li
			1.8550455866666669,  # Li
		]),
		"p": np.array([
			8,  # O
			8,  # O
			8,  # O
			8,  # O
			8,  # O
			8,  # O
			41,  # Nb
			41,  # Nb
			3,  # Li
			3,  # Li
		]),
		"n": np.array([
			7.9994,  # O
			7.9994,  # O
			7.9994,  # O
			7.9994,  # O
			7.9994,  # O
			7.9994,  # O
			51.90638,  # Nb
			51.90638,  # Nb
			3.941,  # Li
			3.941,  # Li
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
