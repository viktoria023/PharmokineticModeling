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
    :param X:      required, [ng] float, the amount of drug administered per injection (if scheme=='dt') or over a chosen time window (if scheme== 'clt')
    :param k_a:    required for sc dosing, [/h] float is the absorption rate
    :param scheme: required, ['clt','dt'], string, pattern of dose administration as specified by user. clt = continous limited time, dt = instantaneous dosage at defined time points
    :param start:  required if scheme=='clt', [h] float, the timepoint at which continous dosage is started. Only used in 'clt'  scheme
    :param stop:   required if scheme=='clt', [h] float, timepoint at which continous dosage is ended. Only used in 'clt'  scheme
    :param tps:    required if scheme=='dt', [h] numpy array, timepoints of instantaneous dose administration in the 'dt' scheme
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
        """Evaluation of Dosage function for the 'dt' scheme
        A continous, smooth instantaneous dosing function is here generated as the sum of gaussian functions with various means.py
        The function approximates "true' instantaneous dosing as the variance of the gaussian (parameter s below) approaches zero/ 
        Parameters
        ----------
        :param t: required, [h] float, timepoint at which to evaluate the dosage function
        
        :returns: float, value of the instantaneous dosage function at timepoint t
        """
        s=0.02 #Variance of each peak. A smaller value results in tighter peaks
        #initialise dose function
        dose=0
        #add peaks at each timepoint
        for t0 in self.tps:
            gaussian=(1/(s*np.sqrt(2*np.pi)))*np.exp(-(t-t0)**2/(2*s**2)) #normalised gaussian (integrates to 1)
            new_peak=self.X*gaussian #scale the peak so that it integrates to the chosen dosage
            dose+=new_peak
        return dose
    def continous_dose(self,t):
        """Evaluation of Dosage function for the continous-limited-time ('clt') scheme
        A continous, smooth continous dosing function is here generated as a smooth approximation of a rectangular function between the chosen strating and stopping timepoint.
        The smooth approximation is here obtained as the product of two sigmoids, and the resulting function approximately integrates to the chosen dose X.
        The approximation becomes better as parameter k is increased.

        Parameters
        ----------
        :param t: required, [h] float, timepoint at which to evaluate the dosage function
        
        :returns: float, value of the continous dosage function at timepoint t
        """

        k=20 #controls the level of approximation of a true rect function
        A=self.X/(self.stop-self.start) #level of the rect function
        sigmoid_1=A/(1+np.exp(-k*(t-self.start)))
        sigmoid_2=-(A/(1+np.exp(-k*(t-self.stop))))+A
        return np.sqrt((sigmoid_1*sigmoid_2))
    def dose(self, t):
        """Definition of dosing scheme
        Depending on the defined dosing scheme, the function determines the value of the dosage function  (Dose(t)) at the required timepoint

        Parameters
        ----------
        :param t: required, [h] float, timepoint at which to evaluate the dose function
        
        :returns: float, value of the dosage function at the specified timepoint t
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
