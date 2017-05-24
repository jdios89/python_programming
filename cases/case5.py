"""
This file contain the case 5
123456789012345678901234567890123456789012345678901234567890123456789012
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  
import lorenz

sigma = 14
beta = 13.0/3.0
rho = 28

parameters = sigma, rho, beta
initial = [1.0, -5.0, 13.0]
lorenz.run.run_lorenz(parameters, ini_state = initial, t = 100, 
                      save = True, fname = 'case_5', 
                      directory = 'case 5')
