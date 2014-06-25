#!/usr/bin/env	python2.7
import numpy as np
import matplotlib.pyplot as plt

Freq=np.array([30,35,40,45,48,49,50,52,55,58,60,62,64,65,70,80,90,95,100,105,110,120,130,140,145,150,160,170])
Db=np.array([75.1,79.4,83.8,91.4,99.3,100.8,101.1,98.8,95.4,93.9,93.1,92.6,92.6,92.5,93.3,97.3,105.7,112.3,113.3,108.9,106,105.6,108.8,117,119.2,118.3,113.8,113.7])
plt.xlabel('Frecuencia')
plt.ylabel('Decibel')
plt.title('DecibelvsFreq a 0.3volts PEGADO')
#for i in range(len(Freq)):
#		plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 370, 50, 130])
plt.plot(Freq,Db,'bo',Freq,Db,'k')
plt.grid(True)
plt.show()
