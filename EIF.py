#import numpy as np
import scipy
import sympy
from sympy import *
from sympy.abc import x,y
m = 511000
U = 1
L = 2
h_ = (.658) * 10 ** (-15)
#express1 = np.tan(np.sqrt((2*m*E)/(h_**2))*L)
#express2 = (-np.sqrt(E/(U-E)))
#soln = nsolve((express1 -express2), E, .15)
#soln = limit(Eq(express1-express2, y),y,0)
print("calculating...")
#print(dsolve(Eq(tan(sqrt((2*m*x)/(h_**2))*L),-sqrt(x/(U-x)),functions=[Eq(y,0)])))
sol1=nsolve((tan(sqrt((2*511000*x)/(.658*10**(-15)))*2)-sqrt((1-x)/x)), 2, dict=true)
sol2=nsolve(Eq(tan(sqrt((2*511000*x)/(.658*10**(-15)))*2),rhs=-sqrt((x/(1-x)))), 2, dict=true)
print(sol1)
print(sol2)
print('done')