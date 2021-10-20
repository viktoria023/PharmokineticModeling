# 2020-software-engineering-projects-pk
This repository solves pharmokinetic models when given the type of model and initial values. 

How to use the repository:

Users will want to provide an input file 'input.txt', which contains the model type (iv or sc for intravenous or subutaneous drug administration respectively), and the desired values for the variables used by the ODE model (Q_p1, V_c, V_p1, CL, X and k_a). The model will then be solved using the scipy solver and plot the drug concentrations in the various compartments over time. A template on how to construct the input file can be found in the repository as 'input_template.txt'.

Developer info (how to get started working with this repository):

The repository has a modular structure, with the user file input.txt being read in the protocol.py file. The protocol.py file then calls the solution.py file with the specified parameters from the input file. The solution.py class has an internal call on the model.py class. The model.py class constructs the model when given the input parameters and returns the corresponding ODE model. The solution class solves the model using the scipy solver and plots the timecourse using matplotlib.
