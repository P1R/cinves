#!/usr/bin/env	python2.7
import numpy as np
import matplotlib.pyplot as plt

Freq=np.array([20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220])
Db=np.array([74,75,85,104,90,90.6,94.6,102.6,110,103.2,103,106.2,104.8,116.2,111.2,111.2,114.9,121,120.3,117.2,118])

plt.xlabel('Frecuencia')
plt.ylabel('Decibel')
plt.title('DecibelvsFreq a 0.3volts')
#for i in range(len(Freq)):
#		plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 330, 50, 130])
plt.plot(Freq,Db,'bo',Freq,Db,'k')
plt.grid(True)
plt.show()
