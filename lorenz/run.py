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
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  
import lorenz.plot as pl
import lorenz.solver as sol
import lorenz.filehandling as fh
import lorenz.util as ut
import matplotlib.pyplot as plt



def run_lorenz(parameters, ini_state = [0.1, 0.1, 0.2], t_d = 1e-3, 
               N = 50000, plot = False, save = False, fname = 'Test', 
               directory = None):
    """
    This function is to run the lorenz simulation, plot it, and save it 
    parameters is a list containing sigma, rho, beta
    ini_state is a vector contaning 
    """
    sigma, rho, beta = parameters
    x, y, z = ini_state
    #t_d = t/N
    #time = [i*t_d for i in range(N)] #get each discrete time
    states = np.array([[x,y,z]]) #create the array
    t = t_d * N
    ti = np.arange(0.0, t, t_d)
    cntr = 1
    for i in ti[:-1]:
        states = np.concatenate((states, 
             [sol.lorenz_solver(states[cntr-1,:], parameters, t_d)]))
        cntr = cntr + 1
        #states = np.concatenate((states, 
        #    [sol.lorenz_solver(states[i-1,:], parameters, t_d)]))
    if plot:
        pl.plot_3d_states(states, save, fname, directory) #plot x,y,z
        pl.plot_2d("xy", states, save, fname, directory) #plot xy
        pl.plot_2d("xz", states, save, fname, directory) #plot xz
        pl.plot_2d("yz", states, save, fname, directory) #plot yz
    if save:
        fh.save_all(fname, sigma, rho, beta, x, y, z, t_d, N, states, 
                    directory)
    return states
         
def load_lorenz(fname = 'Test', plot = True):
    [s2,r3,b2,x2,y2,z2,t_d2,N2,st2] = fh.load_all(fname)
    if plot:
        pl.plot_3d_states(st2)
    return
     
if __name__ == '__main__':
    """
    This is just debugging code
    """
#print("This is a convenient interface for running the simulation \
#     of a lorenz attractor")
    #sigma = ut.my_input_float("sigma") #input all parameters
    #rho = ut.my_input_float("rho")
    #beta = ut.my_input_float("beta")
    #x = ut.my_input_float("x") #input initial conditions
    #y = ut.my_input_float("y")
    #z = ut.my_input_float("z")
    #ini_state = x, y, z
    sigma = 10
    rho = 6
    beta = 8/3
    ini_state = [1.0, 1.0, 1.0]
    t_d = 0.01
    #t = ut.my_input_int("time in seconds") 
    parameters = (sigma, rho, beta)
    N = 80000 #assign 50000 steps as suggested
    t = t_d * N #timestep calculated from simulation time
    #states = np.array([[x,y,z]]) #create the array
    states = np.array([ini_state])
    for i in range(0,N-1):
        states = np.concatenate((states, 
            [sol.lorenz_solver(states[i-1,:], parameters, t_d)]))

    pl.plot_3d_states(states) #plot x,y,z
    #pl.plot_2d("xy", states) #plot xy
    #pl.plot_2d("xz", states) #plot xz
    #pl.plot_2d("yz", states) #plot yz

    #fh.save_all('testo',sigma,rho,beta,x,y,z,t,t_d,states)
    #[s2,r3,b2,x2,y2,z2,t2,t_d2,st2] = fh.load_all('testo')

    #pl.plot_3d_states(st2)
    
    """
    This is for testing. For testing the function. 
    """
    w_states = ut.wikipedia_lorenz([sigma, rho, beta], ini_state, t_d, N, plot = True)
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(w_states[0000:70000,0], w_states[0000:70000,1], w_states[0000:70000,2])
    plt.legend(['wiki'])
    plt.title('Wikipedia')
    plt.show()
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(states[0000:70000,0], states[0000:70000,1], states[0000:70000,2])
    plt.legend(['my'])
    plt.title(' mine')
    plt.show()
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(states[:,0], states[:,1], states[:,2])
    ax.plot(w_states[:,0], w_states[:,1], w_states[:,2])
    plt.legend(['my','wiki'])
    plt.title('Wikipedia vs mine')
    plt.show()
    
    
    ss = states - w_states
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(ss[:,0], ss[:,1], ss[:,2])
    plt.legend(['my'])
    plt.title('diff Wikipedia vs mine')
    plt.show()
#    

#    
#    import numpy as np
#    import matplotlib.pyplot as plt
#    from scipy.integrate import odeint
#    from mpl_toolkits.mplot3d import Axes3D
#
#    rho = 28.0
#    sigma = 10.0
#    beta = 8.0 / 3.0
#
#    def f(state, t):
#        x, y, z = state  # unpack the state vector
#        return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # derivatives
#
#    state0 = [1.0, 1.0, 1.0]
#    t = np.arange(0.0, 40.0, 0.01)
#
#    states = odeint(f, state0, t)
#
#    fig = plt.figure()
#    ax = fig.gca(projection='3d')
#    ax.plot(states[:,0], states[:,1], states[:,2])
#    plt.show()
