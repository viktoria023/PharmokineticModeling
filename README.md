# Small Software Engineering Project: Pharmokinetic Modelling
# DTP 2021 - Group 5

This python library solves and visualises a pharmokinetic model. The user can specify the type of drug adminstration (intravenous or subcutaneouos) and an input file containing values for the model variables (Q_p1, V_c, V_p1, CL, X and k_a; a template file is provided here:  https://github.com/viktoria023/PharmokineticModeling/blob/master/pkmodel/input_template.csv). The model is constructed and solved using SciPy integration solver. A plot is generated to visualise the drug concentrations in various compartments over time. The plot can optionally be saved to a file.

**How to use the package**

python PharmokineticModeling.py

**Developer info (how to get started working with this repository):**

The repository has a modular structure, with the user file input.txt being read in the main.py file. The main file then calls the protocol class to process the input file.  The main file then initiates an object of type Model, that takes the user input as arguments. The model is ultimately solved by initiating an object of type Solution and using the appropriate solver to obtain the timecourse of the intracellular drug concentrations in all compartments. In order to solve the ODEs, th solvers use scipy solver and the final plots of the timecourse are created using matplotlib.

**Links:**

(open in a new tab!)
https://htmlpreview.github.io/?https://raw.githubusercontent.com/viktoria023/PharmokineticModeling/master/docs/source/_build/index.html
