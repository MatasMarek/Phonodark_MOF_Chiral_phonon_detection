"""
    Material properties. For each atom in the primitive cell specify N, S, L, and L^i S^j
    values.

    Note: the order of the parameters must match the phonopy output. For a given material run phonopy
    once and examine the output to get this list

    date && python calculator.py -m inputs/material/mof/mof.py -p inputs/physics_model/light_dark_photon_born.py -n inputs/numerics/standard.py && date
"""
import numpy as np
import src.constants as const

material = "sacsev"

# number of atoms in the primitive cell
num_atoms = 192
mat_properties_dict = {
        # dimension of supercell used in DFT calculation
"supercell_dim": [2.0, 2.0, 2.0],
	"mass":{
		"e": const.M_ELEC,
		"p": const.M_NUCL,
		"n": const.M_NUCL
	},
	"N_list": {
		"e": np.array([
			0.8511447200000001,  # H
			0.8511447200000001,  # H
			0.8511447200000001,  # H
			0.8511447200000001,  # H
			0.8511447200000001,  # H
			0.8511447200000001,  # H
			0.8511447200000001,  # H
			0.8511447200000001,  # H
			5.946310598888888,  # C
			5.946310598888888,  # C
			5.946310598888888,  # C
			5.946310598888888,  # C
			5.946310598888888,  # C
			5.946310598888888,  # C
			5.946310598888888,  # C
			5.946310598888888,  # C
			7.136028023333333,  # N
			7.136028023333333,  # N
			7.136028023333333,  # N
			7.136028023333333,  # N
			18.10371884,  # Cl
			18.10371884,  # Cl
			28.55201163,  # Cu
			28.55201163,  # Cu
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
			17,  # Cl
			17,  # Cl
			29,  # Cu
			29,  # Cu
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
			18.453000000000003,  # Cl
			18.453000000000003,  # Cl
			34.546,  # Cu
			34.546,  # Cu
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
