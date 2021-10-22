import unittest
from model import Model
import numpy as np

class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """
    def test_model_iv_1(self):
        """
        Tests Dosage creation.
        """
        model1 = Model(42, 1.0, 1.0, 1.0, 1.0, 1.0, None, 1, None, None)
        
        #At the moment, function should return X = 1 for any value of t entered
        self.assertEqual(model1.dose(42), 1)

        #Tests if iv model returns a list
        t = np.linspace(0, 1, 100)
        y = np.array([0.0, 0.0])
        self.assertEqual(str(type(model1.ivModel(t,y))), "<class 'list'>")

        #Checks that the list returned has a size of 2
        self.assertEqual(len(model1.ivModel(t,y)), 2)

        #Other test
        self.assertEqual(model1.value, 42)

    def test_model_sc_1(self):
        """
        Tests Dosage creation.
        """
        model2 = Model(42, 1.0, 1.0, 1.0, 1.0, 1.0, None, 1, None, None)

        #Tests if iv model returns a list
        t2 = np.linspace(0, 1, 100)
        y2 = np.array([0.0, 0.0, 0.0])
        self.assertEqual(str(type(model2.scModel(t2,y2))), "<class 'list'>")

        #Checks that the list returned has a size of 3
        self.assertEqual(len(model2.scModel(t2,y2)), 3)

    
