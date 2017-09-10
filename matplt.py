import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt

a = np.arange(0.0, 100.0)
b = np.sin(a)
plt.plot(a, b)
plt.axis([0, 100, -1, 1])
plt.show()