"""
This file can contain functionalities for saving/loading data
"""

import h5py, os

def save_all(fname, sigma, rho, beta, x, y, z, t_d, N, states, directory = None):
    """
    Save the variables, parameters and results in a hdf5 file

    INPUT:: 

     fname:    name of file 
     sigma:    sigma parameter
     rho:    rho parameter
     beta:    beta parameter
     x:    x initial state
     y:    y initial state
     z:    z initial state
     t_d:    time differential
     N:    number of samples
     states:    array of states
     directory:    directory for saving

    OUTPUT::

     A file with all the variables in it. 

    Example: 

    >>> save_all(fname, sigma, rho, beta, x, y, z, t_d, N, states)  
     
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
    f.create_dataset( 't_d', data = t_d)
    f.create_dataset( 'N', data = N)
    f.create_dataset( 'states', data = states)
    f.close()

def load_all(fname):
    """
    
    Save the variables, parameters and results in a hdf5 file

    INPUT:: 

     fname:    name of file

    OUTPUT::
 
     sigma:    sigma parameter
     rho:    rho parameter
     beta:    beta parameter
     x:    x initial state
     y:    y initial state
     z:    z initial state
     t_d:    time differential
     N:    number of samples
     states:    array of states
     
    Example: 

    >>> fname = "experimental"
    >>> [sigma, rho, beta, x, y, z, t_d, N, states] = load_all(fname)  
     
    
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
    return sigma,rho,beta,x,y,z,t_d,N,states

   
