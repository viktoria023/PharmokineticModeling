#
# Protocol class
#
import pandas as pd
import numpy as np

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, csvfile):
        self.csvfile = csvfile
        self.file = pd.read_csv(self.csvfile)
        #Converts data frame to array
        self.vars = self.file.to_numpy()
        #Selects type of model to use: vars = 'iv' or 'sc'
        self.protocol = self.vars[0][1]
        #Raise error if not 'iv' or 'sc'
        if self.protocol not in ['iv','sc']:
            raise TypeError("Model should either be intravenous ('iv') or subcutaneous ('sc')")


        #Could possibly include a test for seeing if correct number of
        #variables is given based on specified model, or a test to
        #check if only 'iv' or 'sc' are given and nothing else

        #Variables for model
        self.model_type = (self.vars[0][1])
        self.Q_p1 = float(self.vars[1][1])
        self.V_c = float(self.vars[2][1])
        self.V_p1 = float(self.vars[3][1])
        self.Cl = float(self.vars[4][1])
        self.x = float(self.vars[5][1])
        self.k_a = float(self.vars[6][1])
        self.scheme = self.vars[7][1]
        self.start=float(self.vars[8][1])
        self.stop = float(self.vars[9][1])
        self.tps = np.fromstring(self.vars[10][1],sep=',')