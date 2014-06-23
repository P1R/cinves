#!/usr/bin/env	python2.7
import numpy as np
import matplotlib.pyplot as plt

A=np.array([0.1,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.5])
Tmin=np.array([0.3,1,1.3,1.8,2.1,2,2.3,3.1,3.6])
DeltaT=np.array([1.2,2.1,3.1,4.1,4.4,4.6,5.2,6.1,6.1])
plt.xlabel('Amplitud (Volts)')
plt.ylabel('Tmin (Celsius)')
plt.title('AmplitudvsDTyTmin')
for i in range(len(A)):
	plt.text(A[i],Tmin[i], r'$Tmin=%f, \ \Delta T=%f$' % (Tmin[i], DeltaT[i]))
	
#plt.text(0.1,0.3, r'$Tmin=0.3,\ \Delta T=1.2$')

plt.axis([0, 0.6, 0, 5])
plt.plot(A,Tmin,'bo',A,Tmin,'k')
plt.grid(True)
plt.show()
