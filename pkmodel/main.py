"""
Where all the files are imported and ran
"""

from model import Model
#from protocol import Protocol
#Probably gonna scrap protocol.py
from solution import Solution

import pandas as pd

#Imports csv and stores as pandas data frame
_vars = pd.read_csv("pkmodel/input_template.csv")

#Converts data frame to array
vars = _vars.to_numpy()
print(vars)

#Selects type of model to use: vars = 'iv' or 'sc'
model = vars[0][1]

#Raise error if not 'iv' or 'sc'
if model not in ['iv','sc']:
    raise TypeError("Model should either be intravenous ('iv') or subcutaneous ('sc')")


#Could possibly include a test for seeing if correct number of
#variables is given based on specified model, or a test to
#check if only 'iv' or 'sc' are given and nothing else

#Variables for model
Q_p1 = vars[1][1]
V_c  = vars[2][1]
V_p1 = vars[3][1]
Cl   = vars[4][1]
x    = vars[5][1]
k_a  = vars[6][1]

t = 1
y = 1

protocol = Model(None,Q_p1,V_c,V_p1,Cl,x,k_a)

if model == 'iv':
    diffs = protocol.ivModel(t,y)
elif model == 'sc':
    diffs = protocol.scModel(t,y)
#diffs is a list.
#If iv, then it'll have 2 elements
#if sc, then 3

print(diffs)

#Getting solutions using differentials
sol = Solution.solve(diffs)

#Graphing
