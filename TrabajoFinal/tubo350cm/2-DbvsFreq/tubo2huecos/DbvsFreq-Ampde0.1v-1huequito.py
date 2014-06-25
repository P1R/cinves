#!/usr/bin/env	python2.7
import numpy as np
import matplotlib.pyplot as plt

Freq=np.array([30,40,45,50,53,55,60,65,70,80,90,95,98,100,110,120])
Db=np.array([70.5,78.6,83.2,88.4,87.5,86.7,85.2,83.9,85.1,88,95.7,100.4,100.4,99.2,94.7,94.9])
plt.xlabel('Frecuencia')
plt.ylabel('Decibel')
plt.title('DecibelvsFreq a 0.1volts')
#for i in range(len(Freq)):
#		plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 330, 50, 130])
plt.plot(Freq,Db,'bo',Freq,Db,'k')
plt.grid(True)
plt.show()
