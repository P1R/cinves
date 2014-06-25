#!/usr/bin/env	python2.7
import numpy as np
import matplotlib.pyplot as plt

Freq=np.array([45,50,55,60,70,80,90,100,110,120,130,140,150,160])
Db=np.array([73.8,86.3,88.2,86,81.5,84,100,104.8,105.6,102.5,106.3,109.1,109.9,105])
plt.xlabel('Frecuencia')
plt.ylabel('Decibel')
plt.title('DecibelvsFreq a 0.3volts PEGADO')
#for i in range(len(Freq)):
#		plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 370, 50, 130])
plt.plot(Freq,Db,'bo',Freq,Db,'k')
plt.grid(True)
plt.show()
