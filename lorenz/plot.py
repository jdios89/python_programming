"""
This file may contain functionalities for plotting
123456789012345678901234567890123456789012345678901234567890123456789012
"""
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

def plot_3d_states(states, save = False, fname = 'experimental', 
                   directory = None):
    """
    This function will plot the 3d behaviour of the lorenz attractor
    states: array of states of the simulation
    """
    fig = plt.figure()
    ax = Axes3D(fig)
    #ax = fig.add_subplot(111, projection='3d')
    #ax = fig.gca(projection='3d')
    #ax = fig.add_subplot(111, projection = '3d')
    ax.plot(states[:,0], states[:,1], states[:,2])
    plt.title('Lorenz Attractor')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    if save:
        if directory != None:
            if not os.path.exists(directory):
                os.makedirs(directory)
            fig.savefig( directory + '/' + fname + '_3d.pdf' )
        else:
            fig.savefig( fname + '_3d.pdf' )
    plt.show()
    return

def plot_2d(selection, states, save = False, fname = 'experimental',
            directory = None):
    """
    This function will plot the selected 2d plot with the given xyz array
    selection: string with the selection
    states: array of xyz coordinates
    """
    plt.figure()
    if selection == "xy":
        """
        PLot xy graph
        """
        plt.plot(states[:,0],states[:,1])
        plt.title("Lorenz Attractor")
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid()
        if save:
            if directory != None:
                if not os.path.exists(directory):
                    os.makedirs(directory)
                plt.savefig( directory + '/' + fname + '_xy.pdf' )
            else:
                plt.savefig( fname + '_xy.pdf' )
        plt.show()
    elif selection == "xz":
        """
        Plot xz graph
        """
        plt.plot(states[:,0],states[:,2])
        plt.title("Lorenz Attractor")
        plt.xlabel('X')
        plt.ylabel('Z')
        plt.grid()
        if save:
            if directory != None:
                if not os.path.exists(directory):
                    os.makedirs(directory)
                plt.savefig( directory + '/' + fname + '_xz.pdf' )
            else:
                plt.savefig( fname + '_xz.pdf' )
        plt.show()
    elif selection == "yz":
        """
        Plot yz graph
        """
        plt.plot(states[:,1],states[:,2])
        plt.title("Lorenz Attractor")
        plt.xlabel('Y')
        plt.ylabel('Z')
        plt.grid()
        if save:
            if directory != None:
                if not os.path.exists(directory):
                    os.makedirs(directory)
                plt.savefig( directory + '/' + fname + '_yz.pdf' )
            else:
                plt.savefig( fname + '_yz.pdf' )
        plt.show()
    else:
        print ("The selection was not correct")
    return
