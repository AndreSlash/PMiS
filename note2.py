import numpy as np
import matplotlib.pyplot as plt
import math
import cmath as cm
from scipy.integrate import odeint

def fun(t, d):
  omega2 = 1.027 # omega = k/m
  c1 = 1
  c2 = 1
  return np.exp(t*(-d-cm.sqrt(d**2-omega2))) * c1 + np.exp(t*(-d+cm.sqrt(d**2-omega2))) * c2

domain=np.linspace(1, 100, 100)

y1 = []
y2 = []

d1=0.1
d2=0.2

for i in domain:
  y1.append(fun(i, d1).astype('float128'))
  y2.append(fun(i, d2).astype('float128'))

fig, ax = plt.subplots()

ax.plot(domain, y1)
ax.plot(domain, y2)

plt.legend(['d=0.1', 'd=0.2'])
plt.show()
