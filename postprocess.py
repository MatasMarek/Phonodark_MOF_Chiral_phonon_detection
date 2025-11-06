import os
from scipy.optimize import curve_fit
import numpy as np
import h5py
import matplotlib.pyplot as plt
import matplotlib


def red_mass(m1, m2):
    return m1 * m2 / (m1 + m2)


def get_index(ele, li, eps=10 ** (-3)):
    """
        Returns the index of the 'closest' element in list to ele.
    """

    index = np.abs(li - ele).argmin()

    diff = np.abs(li[index] - ele)

    if diff > eps:
        print('-- WARNING --')
        print('  Searching data for ele = ' + str(ele)
              + ' and the closest value = ' + str(li[index])
              + ' is not that close.')

    return index


def rebin_1d(array, x_width, new_x_width):
    """
        Rebins a 1d array with previous width x_width and new width, new_x_width.
    """

    if new_x_width < x_width:

        print('--- WARNING ---')
        print('    New x_width <= old x_width and therefore cannot rebin. Returning original array.')

        return array

    elif new_x_width == x_width:

        return array

    else:

        # make sure that the new_x_width is an integer multiple of the x_width
        div_bin_width = int(new_x_width / x_width)

        rebinned_arr = [array[i:i + div_bin_width] for i in range(0, len(array), div_bin_width)]

        for i, ele in enumerate(rebinned_arr):
            if len(ele) != div_bin_width:
                rebinned_arr[i] = np.append(ele, np.zeros(div_bin_width - len(ele)))

        return np.sum(rebinned_arr, axis=1)


def get_masses(filename):
    data = h5py.File(filename, 'r')

    mass_list = data['particle_physics']['dm_properties']['mass_list'][...]

    return mass_list


def PhonoDark_binned_N_SI(filename, mass_eV,
                          energy_bin_width_meV=1.,
                          reference_cs_cm2=10 ** (-40),
                          exposure_kg_year=1.,
                          model='dp'):
    """
        Compute the number of events binned in energy deposition. Default assumptions are a kg-year cross section and reference
        cross section of 10^(-40) cm^2.

        Models: dp - Light dark photon model
                ls - light scalar mediator
                hs - heavy scalar mediator
    """

    data = h5py.File(filename, 'r')

    mass_list = data['particle_physics']['dm_properties']['mass_list'][...]
    mass_index = str(get_index(mass_eV, mass_list))

    raw_binned_rate = data['data']['diff_rate']['0'][mass_index][...]

    rebin_raw_binned_rate = rebin_1d(raw_binned_rate, data['numerics']['energy_bin_width'][...],
                                     energy_bin_width_meV / 10 ** 3) + 10 ** (-100)

    cs_convert_factor = 2568189419.412402
    exp_convert_factor = 2.6876446781285714e+58

    ref_cs = cs_convert_factor * reference_cs_cm2
    exp = exp_convert_factor * exposure_kg_year

    if model == 'dp':
        # dark photon

        m_e = 511 * 10 ** 3  # eV
        alphaEM = 1 / 137

        q0 = alphaEM * m_e

        conversion_factor = ref_cs * exp * np.pi * red_mass(mass_eV, m_e) ** (-2) * (q0) ** 4

    elif model == 'ls':
        # light scalar

        m_n = 938 * 10 ** 6  # eV

        v0_convert_factor = 3.3356409519815205e-06
        v0 = v0_convert_factor * 230

        q0 = mass_eV * v0

        conversion_factor = ref_cs * exp * np.pi * red_mass(mass_eV, m_n) ** (-2) * (q0) ** 4

    elif model == 'hs':
        # heavy scalar

        m_n = 938 * 10 ** 6  # eV

        v0_convert_factor = 3.3356409519815205e-06
        v0 = v0_convert_factor * 230

        conversion_factor = ref_cs * exp * np.pi * red_mass(mass_eV, m_n) ** (-2)

    elif model == 'hdp':
        # heavy scalar

        m_e = 511 * 10 ** 3  # eV
        # m_e = 938 * 10 ** 6  # eV

        v0_convert_factor = 3.3356409519815205e-06
        v0 = v0_convert_factor * 230

        conversion_factor = ref_cs * exp * np.pi * red_mass(mass_eV, m_e) ** (-2)
    else:
        conversion_factor = 1.

    return conversion_factor * rebin_raw_binned_rate


# mass_list = get_masses(dark_photon_data_filename)

# print(PhonoDark_binned_N_SI(dark_photon_data_filename, mass_list[50]))


def PhonoDark_cs_cm2_constraint(filename,
                                threshold_meV=1.,
                                exposure_kg_year=1.,
                                n_cut=3.,
                                model='dp'):
    """
        Returns the 95% C.L. constraint on sigma for all masses assuming a kg-year exposure and 1 meV threshold.
    """

    data = h5py.File(filename, 'r')

    energy_bin_width_meV = 10 ** 3 * data['numerics']['energy_bin_width'][...]

    bin_num_cut = int(threshold_meV / energy_bin_width_meV)

    mass_list = get_masses(filename)

    cs_constraint = []

    for m, mass in enumerate(mass_list):
        binned_rate = PhonoDark_binned_N_SI(filename, mass,
                                            energy_bin_width_meV=energy_bin_width_meV,
                                            reference_cs_cm2=1,
                                            exposure_kg_year=exposure_kg_year,
                                            model=model)

        cs_constraint.append(n_cut / np.sum(binned_rate[bin_num_cut:]))

    return np.array(cs_constraint)


def extrapolate_the_last_part(x, y, xmax, just_extrapolated=False):
    # objective function
    def objective(x, a, b):
        return a * x + b
    x_new = np.linspace(x[-1], np.log10(xmax), 10)
    popt, _ = curve_fit(objective, x[-2:], y[-2:])
    a, b = popt
    y_new = np.array(objective(x_new, a, b))
    if just_extrapolated:
        return x_new, y_new
    else:
        return np.concatenate((x, x_new)), np.concatenate((y, y_new))




