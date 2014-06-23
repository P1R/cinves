#!/usr/bin/env	python2.7
import numpy as np
import matplotlib.pyplot as plt

DT=np.array([0.5,1,1.5,2,2.5,3,3.5,4,4.5])
t=np.array([0.07,0.10,0.13,0.18,0.24,0.32,0.45,1.01,1.36])
plt.ylabel('$\Delta T$')
plt.xlabel('tiempo')
plt.title('$Grafica \Delta T \ vs \ tiempo \ a \ 0.3 \ volts$')
for i in range(len(DT)):
	plt.text(t[i],DT[i], r'$\Delta T=%2.2f \ t=%2.2f$' % (DT[i], t[i]))
plt.axis([0, 2, 0, 5])
plt.plot(t,DT,'bo',t,DT,'k')
plt.grid(True)
plt.show()
