import sympy
from sympy import *
from sympy.solvers.solvers import _tsolve as tsolve
import numpy as np
from sympy.abc import E, x,y
from scipy.optimize import root_scalar,fsolve
m = 511000
U=1
L=2
h_ = (.658)*10**-15
express1 = sympy.tan(sympy.sqrt((2*m*E)/(h_**2))*L)
express2 = (-sympy.sqrt(E/(U-E)))
express3 = (sympy.tan(sympy.sqrt((2*m*E)/(h_**2))*L)) + sympy.sqrt(E/(U-E))
soln = solve(express1 -express2, E)
pprint(print(soln))