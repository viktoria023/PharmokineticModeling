# Small Software Engineering Project: Pharmokinetic Modelling
# DTP 2021 - Group 5

This python library solves and visualises a pharmokinetic model. The user can specify the type of drug adminstration (intravenous or subcutaneouos) and an input file containing values for the model variables (Q_p1, V_c, V_p1, CL, X and k_a; a template file is provided here:  https://github.com/viktoria023/PharmokineticModeling/blob/master/pkmodel/input_template.csv). The model is constructed and solved using SciPy integration solver. A plot is generated to visualise the drug concentrations in various compartments over time. The plot can optionally be saved to a file.

**How to use the package**

python PharmokineticModeling.py

**Developer info (how to get started working with this repository):**

The repository has a modular structure, with the user file input.txt being read in the main.py file. The main file then calls the protocol file which allows to manipulate the dosage (ToDo) and returns only the parameters from the input file that are needed for the specified model (sc or iv). The main file then calls the model file using the output variables of the protocol file and returns the ODEs for the specified model. The output is used to call the solution. The solution class solves the model using the scipy solver and plots the timecourse using matplotlib.

**Links:**

(open in a new tab!)
https://htmlpreview.github.io/?https://raw.githubusercontent.com/viktoria023/PharmokineticModeling/master/docs/source/_build/index.html
