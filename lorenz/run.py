"""
This file may contain a convenient interface/function for 

1: computing a trajectory using an ODE solver from solver.py
2: save data to file
3: plot data
123456789012345678901234567890123456789012345678901234567890123456789012
and possible another function that

2: load data from file
3: plot data

"""
import numpy as np
import solver as sol
import plot as pl
import filehandling as fh
import util as ut

print("This is a convenient interface for running the simulation \
     of a lorenz attractor")
sigma = ut.my_input_float("sigma") #input all parameters
rho = ut.my_input_float("rho")
beta = ut.my_input_float("beta")
x = ut.my_input_float("x") #input initial conditions
y = ut.my_input_float("y")
z = ut.my_input_float("z")
t = ut.my_input_int("time in seconds") 
parameters = (sigma, rho, beta)
N = 50000 #assign 50000 steps as suggested
t_d = t/N #timestep calculated from simulation time
time = [i*t_d for i in range(N)] #get each discrete time
states = np.array([[x,y,z]]) #create the array
for i in range(1,N):
    states = np.concatenate((states, 
            [sol.lorenz_solver(states[i-1,:], parameters, t_d)]))

pl.plot_3d_states(states) #plot x,y,z
pl.plot_2d("xy", states) #plot xy
pl.plot_2d("xz", states) #plot xz
pl.plot_2d("yz", states) #plot yz
