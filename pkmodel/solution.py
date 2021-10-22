#
# Solution class
#
import numpy as np
import scipy.integrate
#from model import *
import matplotlib.pylab as plt

class Solution:
    """A Pharmokinetic (PK) model solution.

    Parameters
    ----------

    :param value:  optional, numeric, an example parameter to test if class can be called correctly
    
    """
    def __init__(self, value=44):
        self.value = value

    def solver_iv(self, modelClass):   

        """A solver for the iv model.

        Takes a specific initialization of the model and calculates the concentration time course.

        Parameters
        ----------

        :object modelClass: required, an object of the type Model. The specific instance of the object is initialized in the main file and passed to the function.

        :returns: bunch SciPy.integrate_ivp object containing arrays t (timepoints) and y (concentration changes)

        """ 
        t_eval = np.linspace(0, 10, 10000)
        y0 = np.array([0.0, 0.0])

        sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: modelClass.ivModel(t, y),
        t_span=[t_eval[0], t_eval[-1]],
        y0=y0, t_eval=t_eval,
        max_step=0.001)
        return sol

    def solver_sc(self, modelClass):
        """A solver for the sc model.

        Takes a specific initialization of the model and calculates the concentration time course.

        Parameters
        ----------

        :object modelClass: required, an object of the type Model. The specific instance of the object is initialized in the main file and passed to the function.

        :returns: bunch SciPy.integrate_ivp object containing arrays t (timepoints) and y (concentration changes)
        """
        t_eval = np.linspace(0, 10, 10000)
        y0 = np.array([0.0, 0.0,0.0])

        sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: modelClass.scModel(t, y),
        t_span=[t_eval[0], t_eval[-1]],
        y0=y0, t_eval=t_eval
        )
        return sol

    #fig = plt.figure()
    def plotter(self, model, sol, model_name, save="no"):
        """A method to visualise the ode solutions using the matplotlib library.

        Parameters
        ----------
        :object sol: required, the ode solution returned by solution.solver_sc or .solver_iv : 
        :param save: required, string, yes or no- if yes, plot saved in PNG
        :param model_name: required, string : "iv" or "sc" 

        :returns: 
                a plot window or an output file, output_plot.png

        """
        self.sol = sol
        self.model_name = model_name
        fig, ax1 = plt.subplots()
        ax1.plot(sol.t, sol.y[0, :], label = model_name + '- q_c',linewidth=3)
        ax1.plot(sol.t, sol.y[1, :], label = model_name + '- q_p1',linewidth=3)
        if model_name=='sc':
            ax1.plot(sol.t, sol.y[2, :], label = model_name + '- q_0',linewidth=3)
        dosage_curve=model.dose(sol.t)
        ax2=ax1.twinx()
        ax2.plot(sol.t,dosage_curve,'--',label='dosage curve',linewidth=2,color='green')
        ax1.legend(loc=1,fontsize=15)
        ax2.legend(loc=2,fontsize=15)
        ax1.set_ylabel('drug mass [ng]',fontsize=15)
        ax2.set_ylabel('drug dosage [ng/h]',fontsize=15)
        ax1.set_xlabel('time [h]',fontsize=15)
        
        if (save == "yes"):
            plt.savefig("output_plot.png")
        else:
            plt.show()