# coding: utf8

from msspec.calculator import MSSPEC
from msspec.utils import hemispherical_cluster, get_atom_index
from ase.build  import bulk
from ase.visualize import view




# Create the copper cubic cell
a0 = 3.6 # The lattice parameter in angstroms
iron = bulk('Fe', a=a0, cubic=True)
cluster = hemispherical_cluster(iron, planes=3, emitter_plane=2)


# Set the absorber (the deepest atom centered in the xy-plane)
cluster.absorber = get_atom_index(cluster, 0, 0, 0)


# Create a calculator for the PhotoElectron Diffration
calc = MSSPEC(spectroscopy='PED')


# Set the cluster to use for the calculation
calc.set_atoms(cluster)


# Run the calculation
data = calc.get_theta_scan(level='2p3/2')


# Show the results
data.view()

# Print the the structures
iron.write('Fe.xyz')
cluster.write('cluster.xyz')


# Save the results to files
data.save('results.hdf5')
data.export('exported_results')


# Clean temporary files
calc.shutdown()
