# importing the required module
import matplotlib.pyplot as plt
from cProfile import label
from pathlib import Path
import numpy as np
import sys
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)


def PrintGraph(plot, x_axis,  y_axis):
    
    plt.bar(x_axis, y_axis)
    # plotting the points

    # function to show the plot

    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')  # works fine on Windows!
    plt.show()  # close the figure to run the next section


def CreateGraph(plots):
    fig = plt.figure()
    plotNumber = 421
    for plot in plots:
        plt1 = fig.add_subplot(plotNumber)
        # plotting the points
        avg = np.average(plot.y)
        plt1.plot(plot.x, plot.y, marker='o',
                  markerfacecolor='blue', markersize=7)
        plt1.axhline(y=avg, color='r', linestyle='--',
                     label='Promedio ('+str(avg)+')')
        plt1.set_title(plot.label)
        plt1.legend()
        plotNumber += 1
    # function to show the plot
    fig.subplots_adjust(hspace=.5, wspace=0.5)
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')  # works fine on Windows!
    plt.show()  # close the figure to run the next section
