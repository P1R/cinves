#!/usr/bin/env	python2.7
import numpy as np
import matplotlib.pyplot as plt

Freq=np.array([30,40,45,48,50,52,55,60,62,65,68,70,80,85,88,90,95,98,100,105,110,120,125,130,140,145,150,160])
Db=np.array([74.7,79.2,84,85.7,90.9,87.3,86.2,84.4,84.2,83.7,82.3,82.9,85.7,88.5,91.1,93.5,98.8,100.9,100.1,96.9,95.9,95.5,94.9,97.2,104,107.7,106.6,102.3])
plt.xlabel('Frecuencia')
plt.ylabel('Decibel')
plt.title('DecibelvsFreq a 0.1volts')
#for i in range(len(Freq)):
#		plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 370, 50, 130])
plt.plot(Freq,Db,'bo',Freq,Db,'k')
plt.grid(True)
plt.show()
