from ase.calculators.lammpslib import LAMMPSlib
import os
import glob



model_dir = os.path.dirname(os.path.realpath(__file__))
name = '0ce218cb3e'
cmds = ['pair_style hybrid/overlay pace table spline 5000',
        f'pair_coeff * * pace {model_dir}/{name}.yace Si', 
        f'pair_coeff 1 1 table {model_dir}/{name}_pairpot.table Si_Si']

calculator = LAMMPSlib(lmpcmds=cmds, keep_alive=True, log_file='lammps_output.log')

no_checkpoint = True
