#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, value, Q_p1=1.0, V_c=1.0, V_p1=1.0, CL=1.0, X=1.0, k_a=None):
        self.value = value
        self.Q_p1=Q_p1
        self.V_c=V_c
        self.V_p1=V_p1
        self.CL=CL
        self.X=X
        self.k_a=k_a

    # this stuff should come from the input to the class

    # simple intravenous model as from prototype.py
    def dose(t, self):
        return self.X

    def ivModel(t, y, self):
        q_c, q_p1 = y
        transition = self.Q_p1 * (q_c / self.V_c - q_p1 / self.V_p1)
        dqc_dt = dose(t, self.X) - q_c / self.V_c * self.CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt]

    # subcutaneous model
    def scModel(t, y, self):
        q_c, q_p1, q_0 = y
        transition = self.Q_p1 * (q_c / self.V_c - q_p1 / self.V_p1)
        dq0_dt = dose(t, self.X) - self.k_a*q_0
        dqc_dt = self.k_a*q_0 - q_c / self.V_c * self.CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt, dq0_dt]

    