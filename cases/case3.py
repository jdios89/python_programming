import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  
import lorenz

sigma = 10
beta = 8.0/3.0
rho = 28

parameters = sigma, rho, beta
initial = [1.0, -5.0, 13.0]
lorenz.run.run_lorenz(parameters, ini_state = initial, t = 100, save = True, 
                      fname = 'case_3', directory = 'case 3')
