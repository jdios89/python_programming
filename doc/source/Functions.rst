###############################################################
The modules and functions in the lorenz package are listed here
###############################################################

Solver: lorenz attractor solver 
=====================================================

Intro
-----

It includes a basic solver for the lorenz attractor.  


Functions
---------

.. automodule:: lorenz.solver
   :members:

Details
-------
**Solver** .- It solves the differential equations with a first
order euler approach which explicit math is depicted below.  

.. math::
   [x_{n+1}, y_{n+1}, z_{n+1}] = [t_d \sigma  (y_n - x_n) + x_n, t_d  ( x_n  ( \rho - z_n) - y_n) + y_n, t_d (x_n y_n - \beta  z_n ) + z_n]


Code
----
.. literalinclude :: ../../lorenz/solver.py

Plot: functions for plotting
=====================================================

Functions
---------

.. automodule:: lorenz.plot
   :members:

Code
----

.. literalinclude :: ../../lorenz/plot.py

File Handling: File handling for saving data for reproducible research
======================================================================

Functions
---------

.. automodule:: lorenz.filehandling
   :members:

Code
----

.. literalinclude :: ../../lorenz/filehandling.py

Run: Code for running all together
==================================

Functions
---------

.. automodule:: lorenz.run
   :members:

Code
----

.. literalinclude :: ../../lorenz/run.py

Util: Utility code
==================

Functions
---------

.. automodule:: lorenz.util
   :members:

Code
----

.. literalinclude :: ../../lorenz/util.py


