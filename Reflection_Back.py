import numpy as np
import matplotlib.pyplot as plt
from bruges.reflection.reflection import zoeppritz_element
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


def comp_vs(vp, sigma):
    return (vp/np.sqrt(2*(sigma - 1)/(2*sigma - 1)))


def calc_Rpp(c1, b1, rho1, c2, b2, rho2, elem):
    theta=np.arange(0, 90, 1)
    return zoeppritz_element(c1, b1, rho1, c2, b2, rho2, theta, elem) 


def computeAndShow(Rpp, wave, title, xLabel, yLabel, path):
# the main Tkinter window
    window = Tk()
    window.title('Plot')
    window.geometry("600x500")

    theta=np.arange(0, 90, 1)
    ticks = [i for i in range(0, 91, 10)]

    # the figure that will contain the plot
    fig = Figure(figsize = (6, 4),
                 dpi = 100)
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.plot(theta, np.real(Rpp), label=wave + ' reflection')
    plot1.plot(theta, -np.imag(Rpp), label=wave + ' reflection imag')
    plot1.plot(theta, np.abs(Rpp), label=wave + ' reflection abs')
    
    if xLabel:
        plot1.set_xlabel(xLabel)
    if yLabel:
        plot1.set_ylabel(yLabel)
    
    plot1.set_xticks(ticks)
    
    if title:
        plot1.set_title(title)  
    
    plot1.legend()
    
    if path:
        plot1.figure.savefig(path + '/' + title + '.png', dpi=300)
    
    # creating the Tkinter canvas containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()    
    
    # run the gui
    window.resizable(False, False) # forbid window's resize
    window.mainloop()
    




if __name__ == "__main__":
    Rpp = calc_Rpp(1500, 0, 1000, 3000, comp_vs(3000, 0.333), 1000, 'PdPu')

    computeAndShow(Rpp, 'PP', 'Hello', 'Angles', 'Rpp', 'C:/Users/Tamara/Desktop/Python Shalaeva')

