"""
This file may contain utility functionalities to the extend you will 
need it
123456789012345678901234567890123456789012345678901234567890123456789012
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D




def my_input_float(var):
    """
    This function is for validation of entering a float value
    """
    while True:
        try:
            variable = float(input("Please enter "+ var +": "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    return variable

def my_input_int(var):
    """
    This function is for validation of entering a float value
    """
    while True:
        try:
            variable = int(input("Please enter "+ var +": "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    return variable

def wikipedia_lorenz(parameters, ini_state = [1.0, 1.0, 1.0],
                     t_d = 8e-4, N = 50000, plot = False):
    """
    This is a Lorenz attractor taken from the wikipedia page 
    It will solve the lorenz attractor with a built-in solver
    odeint of numpy
    """
    sigma, rho, beta = parameters
    x, y, z = ini_state
    #t_d = t/N

    def f(state, t):
        x, y, z = state  # unpack the state vector
        return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # derivatives

    
    t_t = t_d * N
    t = np.arange(0.0, t_t, t_d)

    states = odeint(f, ini_state, t)
    if plot:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot(states[:,0], states[:,1], states[:,2])
        plt.title('Wikipedia Lorenz Attractor')
        plt.show()
    return states
