import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)
k=1
t = np.arange(0.0, 5.0, 0.01)
s = (np.cos(t))**2
#s = 2*np.cos(2*np.pi*380*t)*np.sin(2*np.pi*380)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
		            arrowprops=dict(facecolor='black', shrink=0.05),
			                )

plt.ylim(-2,2)
plt.show()
