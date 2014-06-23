#!/usr/bin/env	python2.7
import numpy as np
import matplotlib.pyplot as plt

Freq=np.array([50,60,70,80,85,90,100,105,110,120,130,140,150,155,160,165,170,180,190,195,200,210,220,230,235,240,245,250,260,270,300])
Db=np.array([70,76.6,84.4,92.6,91.4,90.2,88.5,88.8,89.3,90.4,93,96.8,102.4,105.5,106.3,104.3,102.8,101.3,100.5,100.8,101.4,103.5,106.4,109.8,110.9,111,111,110.8,109.9,109.9,108.7])

plt.xlabel('Frecuencia')
plt.ylabel('Decibel')
plt.title('DecibelvsFreq a 0.1volts')

for i in range(len(Freq)):
		plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 310, 70, 120])
plt.plot(Freq,Db,'bo',Freq,Db,'k')
plt.grid(True)
plt.show()
