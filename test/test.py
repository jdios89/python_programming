"""
In this file you may have your tests


"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  
import lorenz
import unittest
import numpy as np


class Test_solver(unittest.TestCase):
    """
    Test 
    """
    def test_solver1(self):
        """
        The test for my solver 1
        """
        state = [1.0, 1.0, 1.0]
        sig = 10
        ro = 6
        bet = 8/3
        param = [sig, ro, bet]
        t_d = 0.001
        N = 50000
        states = lorenz.run.run_lorenz(param, state, t_d, N)
        w_states = lorenz.util.wikipedia_lorenz(param, state, t_d, N)
        #self.assertAlmostEqual(states.tolist(), w_states.tolist())
        self.assertTrue(np.allclose(states, w_states, 
                                    rtol = 1e-2, atol = 1e-2))
    def test_solver2(self):
        """
        The test for my solver 2
        """
        state = [1.0, -5.0, 13.0]
        sig = 10
        ro = 16
        bet = 8/3
        param = [sig, ro, bet]
        t_d = 0.001
        N = 50000
        states = lorenz.run.run_lorenz(param, state, t_d, N)
        w_states = lorenz.util.wikipedia_lorenz(param, state, t_d, N)
        #self.assertAlmostEqual(states.tolist(), w_states.tolist())
        self.assertTrue(np.allclose(states, w_states, 
                                    rtol = 2e-1,atol = 1))
    def test_solver3(self):
        """
        The test for my solver 3
        """
        state = [1.0, -5.0, 13.0]
        sig = 10
        ro = 28
        bet = 8/3
        param = [sig, ro, bet]
        t_d = 0.0001
        N = 50000
        states = lorenz.run.run_lorenz(param, state, t_d, N)
        w_states = lorenz.util.wikipedia_lorenz(param, state, t_d, N)
        #self.assertAlmostEqual(states.tolist(), w_states.tolist())
        self.assertTrue(np.allclose(states, w_states, 
                                    rtol = 2e-1, atol = 1))

    def test_solver4(self):
        """
        The test for my solver 4
        """
        state = [1.0, -5.0, 13.0]
        sig = 14
        ro = 28
        bet = 8/3
        param = [sig, ro, bet]
        t_d = 0.0001
        N = 50000
        states = lorenz.run.run_lorenz(param, state, t_d, N)
        w_states = lorenz.util.wikipedia_lorenz(param, state, t_d, N)
        #self.assertAlmostEqual(states.tolist(), w_states.tolist())
        self.assertTrue(np.allclose(states, w_states, 
                                    rtol = 2e-1, atol = 1))

    def test_solver5(self):
        """
        The test for my solver 5
        """
        state = [1.0, -5.0, 13.0]
        sig = 14
        ro = 28
        bet = 13/3
        param = [sig, ro, bet]
        t_d = 0.0001
        N = 50000
        states = lorenz.run.run_lorenz(param, state, t_d, N)
        w_states = lorenz.util.wikipedia_lorenz(param, state, t_d, N)
        #self.assertAlmostEqual(states.tolist(), w_states.tolist())
        self.assertTrue(np.allclose(states, w_states, 
                                    rtol = 2e-1, atol = 1))
if __name__ == '__main__':
    unittest.main()
