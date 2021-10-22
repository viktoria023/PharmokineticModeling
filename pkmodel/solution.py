#
# Solution class
#
import numpy as np
import scipy
#from model import *
import matplotlib.pylab as plt

class Solution:
    """A Pharmokinetic (PK) model solution.

    Parameters
    ----------

    :param value:  numeric, an example parameter to test if class can be called correctly
    """
    def __init__(self, value=44):
        self.value = value

    def solver_iv(self, modelClass):   
        """A solver for the iv model.

        Takes a specific initialization of the model and calculates the concentration time course.

        Parameters
        ----------

        :param modelClass: class, an object of the type Model. The specific instance of the object is initialized in the main file and passed to the function.

        :returns: bunch SciPy.integrate_ivp object containing arrays t (timepoints) and y (concentration changes)
        """ 
        t_eval = np.linspace(0, 1, 1000)
        y0 = np.array([0.0, 0.0])

        sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: modelClass.ivModel(t, y),
        t_span=[t_eval[0], t_eval[-1]],
        y0=y0, t_eval=t_eval
        )
        return sol

    def solver_sc(self, modelClass):
        """A solver for the sc model.

        Takes a specific initialization of the model and calculates the concentration time course.

        Parameters
        ----------

        :param modelClass: class, an object of the type Model. The specific instance of the object is initialized in the main file and passed to the function.

        :returns: bunch SciPy.integrate_ivp object containing arrays t (timepoints) and y (concentration changes)
        """
        t_eval = np.linspace(0, 1, 1000)
        y0 = np.array([0.0, 0.0])

        sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: modelClass.scModel(t, y),
        t_span=[t_eval[0], t_eval[-1]],
        y0=y0, t_eval=t_eval
        )
        return sol

    #fig = plt.figure()
    def plotter(self, sol, model_name, save="no"):
        """A method to visualise the ode solutions using the matplotlib library.

        :parameters: 
                sol, required, object : the ode solution returned by solution.solver_sc or solver_iv : 
                save, required, string, yes or no- if yes, plot saved in PNG
                model_name, string, required : "iv" or "sc" 

        :returns: 
                a plot window or a an output file, output_plot.png
        """
        self.sol = sol
        self.model_name = model_name
        fig = plt.figure()
        plt.plot(sol.t, sol.y[0, :], label = model_name + '- q_c')
        plt.plot(sol.t, sol.y[1, :], label = model_name + '- q_p1')
        plt.legend()
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        
        if (save == "yes"):
            plt.savefig("output_plot.png")
        else:
            plt.show()