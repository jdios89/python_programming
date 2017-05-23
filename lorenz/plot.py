"""
This file may contain functionalities for plotting
123456789012345678901234567890123456789012345678901234567890123456789012
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

def plot_3d_states(states, save = False, fname = 'experimental'):
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
    if save:
        fig.savefig( fname + '_3d.pdf' )
    plt.show()
    return

def plot_2d(selection, states, save = False, fname = 'experimental'):
    """
    This function will plot the selected 2d plot with the given xyz array
    selection: string with the selection
    states: array of xyz coordinates
    """
    if selection == "xy":
        """
        PLot xy graph
        """
        plt.plot(states[:,0],states[:,1])
        plt.title("XY graph")
        if save:
            plt.savefig( fname + '_xy.pdf')
        plt.show()
    elif selection == "xz":
        """
        Plot xz graph
        """
        plt.plot(states[:,0],states[:,2])
        plt.title("XZ graph")
        if save:
            plt.savefig( fname + '_xz.pdf')
        plt.show()
    elif selection == "yz":
        """
        Plot yz graph
        """
        plt.plot(states[:,1],states[:,2])
        plt.title("YZ graph")
        if save:
            plt.savefig( fname + '_yz.pdf')
        plt.show()
    else:
        print ("The selection was not correct")
    return
