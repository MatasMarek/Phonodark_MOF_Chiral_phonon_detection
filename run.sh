#!/bin/bash

#SBATCH --job-name phonodark
#SBATCH --output job.out
#SBATCH --error job.err
#SBATCH --nodes=1
#SBATCH --tasks-per-node=128
#SBATCH --time 48:00:00


exe=/PhonoDark-master
path_calc=/PhonoDark-master

module --force purge
cd $exe/
echo "Starting"

source $exe/venv/bin/activate
ml mpi4py/3.1.5-gompi-2023b

cd $path_calc

echo "Running"
python3.11 -u $exe/calculator_haxxored.py -m $exe/inputs/material/linbo3/input.py -p $exe/inputs/physics_model/o1_heavy_leptophilic_born.py -n $exe/inputs/numerics/standard.py > phonodark.out 2>phonodark.err
echo "Done"
