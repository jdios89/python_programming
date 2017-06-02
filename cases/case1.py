"""
This file contain the case 1
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  
import lorenz

sigma = 10
beta = 8.0/3.0
rho = 6

parameters = sigma, rho, beta
initial = [1.0, -2.0, 3.0]
lorenz.run.run_lorenz(parameters, ini_state = initial, t_d = 0.001, 
                      plot = True, save = True, fname = 'case_1', 
                      directory = 'case 1')
