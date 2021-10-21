# 2020-software-engineering-projects-pk
This repository solves pharmokinetic models when given the type of model and initial values. 

How to use the repository:

Users will want to provide an input file 'input.txt', which contains the model type (iv or sc for intravenous or subutaneous drug administration respectively), and the desired values for the variables used by the ODE model (Q_p1, V_c, V_p1, CL, X and k_a). The model will then be constructed and solved using the scipy solver. The user will be provided with a plot of the drug concentrations in the various compartments over time. A template on how to construct the input file can be found in the repository as 'input_template.txt'. The whole model can be run by simply using the main.py file.

Developer info (how to get started working with this repository):

The repository has a modular structure, with the user file input.txt being read in the main.py file. The main file then calls the protocol file which allows to manipulate the dosage (ToDo) and returns only the parameters from the input file that are needed for the specified model (sc or iv). The main file then calls the model file using the output variables of the protocol file and returns the ODEs for the specified model. The output is used to call the solution. The solution class solves the model using the scipy solver and plots the timecourse using matplotlib.
