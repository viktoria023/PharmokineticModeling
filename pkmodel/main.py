"""
Where all the files are imported and ran
"""

from model import Model
from solution import Solution
from protocol import Protocol
import pandas as pd

#Imports csv and stores as pandas data frame
UserVariables = Protocol("input_template.csv")

modelClass = Model(None, UserVariables.Q_p1, UserVariables.V_c, UserVariables.V_p1, UserVariables.Cl, UserVariables.x, UserVariables.k_a, UserVariables.scheme,UserVariables.start, UserVariables.stop, UserVariables.tps)

solution=Solution()

if UserVariables.protocol== 'iv':
    sols =solution.solver_iv(modelClass)

elif UserVariables.protocol == 'sc':
    sols = solution.solver_sc(modelClass)

solution.plotter(modelClass,sols, 'iv', 'no')