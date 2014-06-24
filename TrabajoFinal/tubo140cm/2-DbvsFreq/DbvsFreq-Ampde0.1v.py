#!/usr/bin/env	python2.7
import numpy as np
import matplotlib.pyplot as plt

Freq=np.array([20,40,60,80,100,120,125,140,160,180,200,220,240,250,260,280,300,340,360,370,380,390,400,420])
Db=np.array([70,71.4,80.1,88.2,98.1,108.8,107.4,104.1,103.2,105.5,109.6,114.8,117.2,117.1,117.1,117.3,116.2,115.2,118.8,123.4,126.3,122.4,118,117.8])
plt.xlabel('Frecuencia')
plt.ylabel('Decibel')
plt.title('DecibelvsFreq a 0.1volts')
#for i in range(len(Freq)):
#	plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 430, 50, 130])
plt.plot(Freq,Db,'bo',Freq,Db,'k')
plt.grid(True)
plt.show()
