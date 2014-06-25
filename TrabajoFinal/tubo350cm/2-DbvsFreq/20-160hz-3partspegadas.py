#!/usr/bin/env	python2.7
import numpy as np
import matplotlib.pyplot as plt

Freq=np.array([30,35,40,45,48,49,50,52,55,58,60,62,64,65,70,80,90,95,100,105,110,120,130,140,145,150,160])
Db=np.array([72.2,76.5,81,88.8,95.7,97.4,97.2,95.6,93,91,90.5,90.1,90.1,90.1,90.9,94.9,102.8,109.5,110.7,106.1,103.5,103.2,106.3,114.7,118,116.6,111.3])
plt.xlabel('Frecuencia')
plt.ylabel('Decibel')
plt.title('DecibelvsFreq a 0.3volts PEGADO')
#for i in range(len(Freq)):
#		plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 370, 50, 130])
plt.plot(Freq,Db,'bo',Freq,Db,'k')
plt.grid(True)
plt.show()
