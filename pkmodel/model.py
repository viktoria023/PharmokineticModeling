#
# Model class
#

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
    def __init__(self, value=42, Q_p1=1.0, V_c=1.0, V_p1=1.0, CL=1.0, X=1.0, k_a=None, stop=None, scheme=None, tps=None):
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
        """Definition of dosing scheme.

        Depending on the defined dosing scheme, the function determines the released dosage X at the  specified timepoint. 

        Parameters
        ----------
        :param t: required, [h] float, timepoint tested by dose function
        
        :returns: float, amount of drug released at the specified timepoint t
        """
        if self.scheme=='clt' and t<self.stop:
            return self.X
        elif self.scheme=='hlt':
            if t%1==0 and t<self.stop:
                return self.X
        elif self.scheme=='dt':
            if t in self.tps:
                return self.X
        return 0

    def ivModel(t, y, self):
        """Setting up intravenous model.

        Sets up 2-compartment model 

        Parameters
        ----------
        :param t: required, [h] float, current timepoint 
        :param y: required, [ng, ng] list, current amount of drug in the compartments

        :returns: list, change of drug concentrations in respective compartments as a derivative of the time
        """
        q_c, q_p1 = y
        transition = self.Q_p1 * (self.q_c / self.V_c - q_p1 / self.V_p1)
        dqc_dt = self.dose(t, self.X) - q_c / self.V_c * self.CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt]

    # subcutaneous model
    def scModel(t, y, self):
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
        dq0_dt = self.dose(t, self.X) - k_a*q_0
        dqc_dt = k_a*q_0 - q_c / self.V_c * self.CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt, dq0_dt]
