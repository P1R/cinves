#!/usr/bin/env	python2.7
import numpy as np
import matplotlib.pyplot as plt

Freq=np.array([20,30,40,45,48,50,52,55,60,62,65,68,70,80,85,88,90,95,98,100,105,110,120,125,130,140,145,160])
Db=np.array([81.7,85.1,94,103.8,110.8,112.7,110.9,105.8,96.2,95.9,94.7,94.6,95.2,99.2,102.6,105.3,106.9,117.5,119.3,117.3,110.2,108.1,108.4,108.9,109.7,118.6,120,116.8])
plt.xlabel('Frecuencia')
plt.ylabel('Decibel')
plt.title('DecibelvsFreq a 0.5volts')
#for i in range(len(Freq)):
#		plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 370, 50, 130])
plt.plot(Freq,Db,'bo',Freq,Db,'k')
plt.grid(True)
plt.show()
