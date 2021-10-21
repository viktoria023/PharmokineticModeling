#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example parameter to test if class can be called correctly
    

    """
    def __init__(self, value, Q_p1=1.0, V_c=1.0, V_p1=1.0, CL=1.0, X=1.0, k_a=None, stop=None, scheme=None, tps=None):
        self.value = value
        self.Q_p1=Q_p1
        self.V_c=V_c
        self.V_p1=V_p1
        self.CL=CL
        self.X=X
        self.k_a=k_a
        self.stop=stop
        self.scheme=scheme
        self.tps=tps

    def dose(t, self):
        """Definition of dosing scheme
        Depending on the defined dosing scheme, the function returns the defined dosage X
        at the  specified timepoints. 

        Parameters
        ___________
        t: numeric, timepoint tested by dose function
        
        """
        if scheme=='ilt' and t<stop:
            return X
        elif scheme=='hlt':
            if t%1==0 and t<stop:
                return X
        elif scheme=='dt':
            if t in tps:
                return X
        return 0

    def ivModel(t, y, self):
        """Setting up intravenous model
        Sets up 2-compartment model 

        Parameters
        ___________
        t: float, tested timepoint 
        y: array, 

        """
        q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqc_dt = self.dose(t, X) - q_c / V_c * CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt]

    # subcutaneous model
    def scModel(t, y, self):
        """Setting up subcatenous model
        Sets up 2-compartment model 

        Parameters
        ___________
        t: float, tested timepoint 
        y: array, 

        """
        q_c, q_p1, q_0 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dq0_dt = self.dose(t, X) - k_a*q_0
        dqc_dt = k_a*q_0 - q_c / V_c * CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt, dq0_dt]

    