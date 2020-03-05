import matplotlib.pyplot as plt
import numpy as np

def f(t):
    # A*e^(-r/rho) - C/r^6 q1*q2/r
    A = 33652.75
    rho = 0.2646
    C = 259.1
    # q1 = 0.95
    # q2 = 0.95
    # return A * np.exp(-t / rho) - C/t**6 + q1*q2/t
    return A * np.exp(-t / rho) - C/t**6

t1 = np.arange(2.0,7.0,0.1)
plt.plot(t1,f(t1))
plt.show()
