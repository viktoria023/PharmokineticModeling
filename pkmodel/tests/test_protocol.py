from protocol import Protocol

import unittest

test_file_1 = 'test.csv'

class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """
    def test_correct_protocol(self):
        """
        Tests Protocol creation.
        """
        with self.AssertRaises(TypeError):
            main = Protocol(test_file_1)
                

