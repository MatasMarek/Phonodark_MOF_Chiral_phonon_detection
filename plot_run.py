import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from postprocess import PhonoDark_cs_cm2_constraint, get_masses, extrapolate_the_last_part


def plot_reach():
    material = 'linbo3'
    path_to_folder = '' # specify your path here
    model_filename = '' # specify your model here
    dark_photon_data_filename_in = f'{path_to_folder}/data/{material}_{model_filename}_standarddp_testing.hdf5'

    reach = PhonoDark_cs_cm2_constraint(dark_photon_data_filename_in, model=model)
    mass_list = get_masses(dark_photon_data_filename_in)


    plt.plot(mass_list / 10 ** 6, reach, '-', linewidth=2)

    np.savetxt(f'{path_to_folder}/data/{material}_{model_filename}_reach.txt', reach)
    np.savetxt(f'{path_to_folder}/data/{material}_{model_filename}_mass_list.txt', mass_list)

    # Add legend after plotting
    plt.legend(loc='upper left')  # You can adjust the location of the legend if necessary

    plt.tight_layout(pad=0.6)
    plt.savefig('exclusion_plot.pdf')

    plt.show()
    plt.close()
    return


if __name__ == '__main__':
    plot_reach()








