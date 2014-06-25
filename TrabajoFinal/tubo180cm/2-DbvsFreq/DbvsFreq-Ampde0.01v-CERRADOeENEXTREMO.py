#!/usr/bin/env	python2.7
import numpy as np
import matplotlib.pyplot as plt

Freq=np.array([20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320])
Db=np.array([70,76.7,87.1,95.4,94.2,93.2,93.2,93.9,95.4,97.7,101.3,106.3,110.7,106,104.1,103.3,103.1,103.9,105.5,108.0,111.2,113.3,112.3,110.4,109.1,108.4,108.1,108.3,109.1,109.9,112.2])
plt.xlabel('Frecuencia')
plt.ylabel('Decibel')
plt.title('DecibelvsFreq a 0.01volts CERRADO')
#for i in range(len(Freq)):
#	plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 430, 50, 130])
plt.plot(Freq,Db,'bo',Freq,Db,'k')
plt.grid(True)
plt.show()
