"""
Where all the files are imported and ran
"""

from model import Model
from solution import Solution

import pandas as pd

#Imports csv and stores as pandas data frame
_vars = pd.read_csv("pkmodel/input_template.csv")

#Converts data frame to array
vars = _vars.to_numpy()
print(vars)

#Selects type of model to use: vars = 'iv' or 'sc'
protocol = vars[0][1]

#Raise error if not 'iv' or 'sc'
if protocol not in ['iv','sc']:
    raise TypeError("Model should either be intravenous ('iv') or subcutaneous ('sc')")


#Could possibly include a test for seeing if correct number of
#variables is given based on specified model, or a test to
#check if only 'iv' or 'sc' are given and nothing else

#Variables for model
Q_p1 = float(vars[1][1])
V_c  = float(vars[2][1])
V_p1 = float(vars[3][1])
Cl   = float(vars[4][1])
x    = float(vars[5][1])
k_a  = float(vars[6][1])
scheme = vars[7][1]
stop = vars[7][1]
tps = vars[8][1]

modelClass = Model(None,Q_p1,V_c,V_p1,Cl,x,k_a,scheme,stop,tps)

solution=Solution()

if protocol== 'iv':
    sols = solution.solver_iv(modelClass)

elif protocol == 'sc':
    sols = solution.solver_sc(modelClass)

solution.plotter(sols, 'iv', 'no')