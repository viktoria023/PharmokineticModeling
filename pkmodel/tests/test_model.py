import unittest
from model import Model

class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """
    def test_model_iv_1(self):
        """
        Tests Dosage creation.
        """
        model1 = Model(self, value = 42, Q_p1=1.0, V_c=1.0, V_p1=1.0, CL=1.0, X=1.0, k_a=None)
        self.assertEqual(model1.dose, 42)
        self.assertEqual(model1.ivModel, 42)
        self.assertEqual(model1.value, 42)

    def test_model_sc_1(self):
        """
        Tests Dosage creation.
        """
        model1 = Model(self, value = 42 , Q_p1=1.0, V_c=1.0, V_p1=1.0, CL=1.0, X=1.0, k_a=None)
        self.assertEqual(model1.dose, 42)
        self.assertEqual(model1.scModel, 42)
        self.assertEqual(model1.value, 42)
    
