#
# Solution class
#
import numpy as np
import scipy

class Solution:
    """A Pharmokinetic (PK) model solution

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, value=44):
        self.value = value

    def solver_iv(self, modelClass):
        """A solver for the iv model
        Takes the model and calculates the concentration changes as a function of the time

        Parameters
        __________

        modelClass: class, an object of the type model. Defined in main file and 
        has attribute .ivModel that takes t and y as input

        :returns: file with time and concentrations at given time for all compartments in file 'sol'
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
        t_eval = np.linspace(0, 1, 1000)
          y0 = np.array([0.0, 0.0])

        sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: modelClass.scModel(t, y),
        t_span=[t_eval[0], t_eval[-1]],
        y0=y0, t_eval=t_eval
        )
        return sol
