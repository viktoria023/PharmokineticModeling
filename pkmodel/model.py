#
# Model class
#
import numpy as np
class Model:
    """A Pharmokinetic (PK) model.

    Parameters
    ----------

    :argument value:  optional, numeric, an example parameter to test if class can be called correctly
    :param Q_p1:   required, [mL/h] float, the transition rate between central compartment and peripheral compartment 1
    :param V_c:    required, [mL] float, the volume of the central compartment
    :param V_p1:   required, [mL] float, the volume of the first peripheral compartment
    :param CL:     required, [mL/h] float, the clearance/elimination rate from the central compartment
    :param X:      required, [ng] float, the amount of drug administered per injection
    :param k_a:    required for sc dosing, [/h] float is the absorption rate
    :param scheme: required, ['clt','hlt','dt'], string, pattern of dose administration as specified by user. clt = instantaneous limited time, hlt = hourly limited time, dt = defined time points
    :param stop:   required, [h] float, timepoint at which injection stops. Only used in 'ilt' and 'hlt' scheme
    :param tps:    required in 'dt' scheme, [h] float, timepoints of dose administration as specified by the user
    """
    def __init__(self, value=42, Q_p1=1.0, V_c=1.0, V_p1=1.0, CL=1.0, X=1.0, k_a=None,  scheme=None, start=0,stop=None,tps=None):
        self.value = value
        self.Q_p1=Q_p1
        self.V_c=V_c
        self.V_p1=V_p1
        self.CL=CL
        self.X=X
        self.k_a=k_a
        self.start=start
        self.stop=stop
        self.scheme=scheme
        self.tps=tps
    def instantaneous_dose(self,t):
        #Compute the dose function at time t for a instantaneous dosage scheme.
        #The dosage function is computed as a smooth approximation of a train of spikes 
        s=0.05 #controls the width of each pek
        dose=0
        for t0 in self.tps:
            new_peak=self.X*np.exp(-(t-t0)**2/(2*s**2))
            dose+=new_peak
        return dose
    def continous_dose(self,t):
        #Compute the dose function at time t for a continous dosage scheme between a starting and stopping time.
        #The dosage function is computed as a smooth approximation of a boxcar function 
        k=20
        sigmoid_1=self.X/(1+np.exp(-k*(t-self.start)))
        sigmoid_2=-self.X/(1+np.exp(-k*(t-self.stop)))+self.X
        return np.sqrt((sigmoid_1*sigmoid_2))
    def dose(self, t):
        """Definition of dosing scheme
        Depending on the defined dosing scheme, the function determines the released dosage X
        at the  specified timepoint. 

        Parameters
        ----------
        :param t: required, [h] float, timepoint tested by dose function
        
        :returns: float, amount of drug released at the specified timepoint t
        """
        if self.scheme=='clt':
            return self.continous_dose(t)
        elif self.scheme=='dt':
            return self.instantaneous_dose(t)
        else:
            return 0    
   

    def ivModel(self, t, y):
        """Setting up intravenous model

        Sets up 2-compartment model 

        Parameters
        ----------
        :param t: required, [h] float, current timepoint 
        :param y: required, [ng, ng] list, current amount of drug in the compartments

        :returns: list, change of drug concentrations in respective compartments as a derivative of the time
        """
        q_c, q_p1 = y
        transition = self.Q_p1 * (q_c / self.V_c - q_p1 / self.V_p1)
        dqc_dt = self.dose(t) - q_c / self.V_c * self.CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt]

    # subcutaneous model
    def scModel(self, t, y):
        """Setting up subcatenous model

        Sets up 3-compartment model, with inital compartment giving off the drug to the central compartment at rate k_a

        Parameters
        ----------
        :param t: required, [h] float, current timepoint 
        :param y: required, [ng, ng, ng] list, current amount of drug in the compartments

        :returns: list, change of drug concentrations in respective compartments as a derivative of the time
        """
        q_c, q_p1, q_0 = y
        transition = self.Q_p1 * (q_c / self.V_c - q_p1 / self.V_p1)
        dq0_dt = self.dose(t) - self.k_a*q_0
        dqc_dt = self.k_a*q_0 - q_c / self.V_c * self.CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt, dq0_dt]
