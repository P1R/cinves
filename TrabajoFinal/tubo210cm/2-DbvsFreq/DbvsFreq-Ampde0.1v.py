#!/usr/bin/env	python2.7
import numpy as np
import matplotlib.pyplot as plt

Freq=np.array([60,70,75,80,85,90,100,105,110,130,140,145,150,155,160,165,180,190,200,230,235,240,245,250,260,280,300])
Db=np.array([78.5,86.3,91.3,96.1,95.8,93.4,91.1,90.9,91.1,94.8,98.7,100.5,104,107.5,109.1,107.7,103.7,102.9,103.6,112,112.9,113.3,113,112.8,112.1,111.8,111.4])

plt.xlabel('Frecuencia')
plt.ylabel('Decibel')
plt.title('DecibelvsFreq a 0.1volts')

for i in range(len(Freq)):
		plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 310, 70, 120])
plt.plot(Freq,Db,'bo',Freq,Db,'k')
plt.grid(True)
plt.show()
