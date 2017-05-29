"""
This file can contain functionalities for saving/loading data
123456789012345678901234567890123456789012345678901234567890123456789012
"""

import h5py, os

def save_all(fname, sigma, rho, beta, x, y, z, t, t_d, states, directory = None):
    """
    This function is to save all data in a HDF5 interface. The data 
    comprises configuration variables and the solution for the given 
    data
    """
    if directory != None:
        if not os.path.exists(directory):
            os.makedirs(directory)
        f = h5py.File( directory + '/' + fname + '.hdf5', 'w')
    else:
        f = h5py.File( fname + '.hdf5', 'w')
        
    f.create_dataset( 'sigma', data = sigma)
    f.create_dataset( 'rho', data = rho)
    f.create_dataset( 'beta', data = beta)
    f.create_dataset( 'x', data = x)
    f.create_dataset( 'y', data = y)
    f.create_dataset( 'z', data = z)
    f.create_dataset( 't_d', data = t)
    f.create_dataset( 'N', data = t_d)
    f.create_dataset( 'states', data = states)
    f.close()

def load_all(fname):
    """
    This function is to load all the variables
    """
    f = h5py.File( fname + '.hdf5', 'r')
    sigma = f [ 'sigma' ]
    sigma = sigma [...]
    rho = f [ 'rho' ]
    rho = rho [...]
    beta = f [ 'beta' ]
    beta = beta [...]
    x = f [ 'x' ]
    x = x [...]
    y = f [ 'y' ]
    y = y [...]
    z = f [ 'z' ]
    z = z [...]
    t_d = f [ 't_d' ]
    t_d = t_d [...]
    N = f [ 'N' ]
    N = N [...]
    states = f [ 'states' ]
    states = states [...]
    return sigma,rho,beta,x,y,z,t,t_d,states

   