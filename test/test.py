"""
In this file you may have your tests


"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  
import lorenz
import unittest

class Test_solver(unittest.TestCase):
    """
    Test 
    """
    def test_solver(self):
        """
        The test for my solver
        """
        state = [1.0, 1.0, 1.0]
        sig = 10
        ro = 28
        bet = 2.6
        param = [sig, ro, bet]
        td = 0.002
        x,y,z = lorenz.solver(state, param, td)
        self.assertEqual([x,y,z], odeint())