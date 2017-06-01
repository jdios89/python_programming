"""
This is the solver for the differential equations of Lorenz attractor. 
"""

def lorenz_solver(state, parameters, t_d):
    """
    
    Returns the array of x,y,z value after solving the ODE of the lorenz
    attractor using the Euler approach. 

    INPUT::

     state:    x,y,z state
     parameters:    sigma, rho, beta parameters
     t_d:    the time step for the discrete integration

    OUTPUT::

     [x+1, y+1, z+1]:    The next x,y,z values

    It is more accurate when it is close to the convergence point of the
    attractor. 

    Example: 

    >>> state = [1.0, 1.0, 1.0]
    >>> parameters = [1.0, 1.0, 1.0]
    >>> t_d = 0.001
    >>> lorenz_solver(state, parameters, t_d)
    (1.0, 0.999, 1.0)
    
    """
    x, y, z = state # get the state
    sigma, rho, beta = parameters # get the parameters
    return t_d * sigma * (y - x) + x, t_d * ( x * (rho - z) - y) + y, \
           t_d * (x * y - beta * z ) + z

