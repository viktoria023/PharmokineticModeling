from protocol import Protocol
import pandas as pd

import unittest

test_file_1 = '../input_template.csv'

class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """
    def test_correct_protocol(self):
        """
        Tests Protocol creation.
        """
        with unittest.AssertRaises(TypeError):
            main = Protocol(test_file_1)
                

