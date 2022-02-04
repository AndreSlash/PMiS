import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import odeint

omega = 1.0333
delta = 0.072
tmax = 100

def fun(u,x):
  return (u[1], (-(2*delta) * u[1]) - omega**2 * u[0])

x0 = [2,0]
xs = np.linspace(0,tmax,600)
us = odeint(fun, x0, xs)

plt.plot(us[:,0], us[:,1])
plt.show()
