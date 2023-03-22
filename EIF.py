import sympy
from sympy import *
import numpy as np
from sympy.abc import x, y
from scipy.optimize import root_scalar,fsolve
m = 511000
E=1
h_ = (.658)*10**-15
express1 = sympy.tan(sympy.sqrt((2*m*E)/(h_**2))*x)
express2 = (-sympy.sqrt(E/(x-E)))
#express1= sympy.cos(x)
#express2= sympy.sin(sympy.sqrt((5*x)/(4*x)**2))
#domain = [1 < x, x <= 2]
#eq1 = Eq(express1, express2)
#print(str(sympy.tan(sympy.sqrt((2*m*E)/(h_**2))*1.847)))
print(solve([Eq(express2,express1)], x, domain=[1,2]), particular = True, quick= True)