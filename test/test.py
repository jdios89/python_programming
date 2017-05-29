"""
In this file you may have your tests


"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  
import lorenz
import unittest
import numpy as np
import matplotlib.pyplot as plt

class Test_solver(unittest.TestCase):
    """
    Test 
    """
    def test_solver1(self):
        """
        The test for my solver
        """
        state = [1.0, 1.0, 1.0]
        sig = 10
        ro = 6
        bet = 8/3
        param = [sig, ro, bet]
        t_d = 0.001
        N = 100000
        states = lorenz.run.run_lorenz(param, state, t_d, N)
        w_states = lorenz.util.wikipedia_lorenz(param, state, t_d, N)
        #self.assertAlmostEqual(states.tolist(), w_states.tolist())
        self.assertTrue(np.allclose(states, w_states, 
                                    atol = 1e-2, rtol = 1e-2))
    def test_solver2(self):
        """
        The test for my solver
        """
        """
        The test for my solver
        """
        state = [1.0, 1.0, 1.0]
        sig = 10
        ro = 16
        bet = 8/3
        param = [sig, ro, bet]
        t_d = 0.001
        N = 100000
        states = lorenz.run.run_lorenz(param, state, t_d, N)
        w_states = lorenz.util.wikipedia_lorenz(param, state, t_d, N)
        #self.assertAlmostEqual(states.tolist(), w_states.tolist())
        self.assertTrue(np.allclose(states, w_states, 
                                    atol = 1, rtol = 1))
    def test_solver3(self):
        """
        The test for my solver
        """
        state = [1.0, 1.0, 1.0]
        sig = 10
        ro = 28
        bet = 8/3
        param = [sig, ro, bet]
        t_d = 0.001
        N = 100000
        states = lorenz.run.run_lorenz(param, state, t_d, N)
        w_states = lorenz.util.wikipedia_lorenz(param, state, t_d, N)
        #self.assertAlmostEqual(states.tolist(), w_states.tolist())
        self.assertTrue(np.allclose(states, w_states, 
                                    atol = 1, rtol = 1))
if __name__ == '__main__':
    unittest.main()
