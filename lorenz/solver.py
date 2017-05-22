"""
This file contain the ODE solver
123456789012345678901234567890123456789012345678901234567890123456789012
"""

def lorenz_solver(state, parameters, t_d):
    """
    This is an Euler solver for the lorenz attractor
    state: contains the x,y,z state
    parameters: contains the sigma, rho, beta parameters
    t_d: the time step for the discrete integration
    """
    x, y, z = state # get the state
    sigma, rho, beta = parameters # get the parameters
    return t_d * sigma * (y - x) + x, t_d * ( x * (rho - z) - y) + y, \
           t_d * (x * y - beta * z ) + z


