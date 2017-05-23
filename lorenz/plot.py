"""
This file may contain functionalities for plotting
123456789012345678901234567890123456789012345678901234567890123456789012
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

def plot_3d_states(states):
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
    fig.savefig( 'states3d.pdf' )
    plt.show()
    return

def plot_2d(selection, states):
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
        plt.savefig('states2dxy.pdf')
        plt.show()
    elif selection == "xz":
        """
        Plot xz graph
        """
        plt.plot(states[:,0],states[:,2])
        plt.title("XZ graph")
        plt.savefig('states2dxz.pdf')
        plt.show()
    elif selection == "yz":
        """
        Plot yz graph
        """
        plt.plot(states[:,1],states[:,2])
        plt.title("YZ graph")
        plt.savefig('states2dyz.pdf')
        plt.show()
    else:
        print ("The selection was not correct")
    return
