#!/usr/bin/env	python2.7
import numpy as np
import matplotlib.pyplot as plt

Freq=np.array([20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350])
Db=np.array([75,72.7,77.1,82.7,88.8,94,102,111.1,108.7,105.4,104.4,105.2,106.9,109.4,112.8,118.4,121.2,120.4,118.2,117.4,117.0,118.1,119.7,121.7,123.2,124.2,125.0,125.2,124.9,123.7,122.4,121.1,121.1,122.0])
plt.xlabel('Frecuencia')
plt.ylabel('Decibel')
plt.title('DecibelvsFreq a 0.3volts')
#for i in range(len(Freq)):
#	plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 430, 50, 130])
plt.plot(Freq,Db,'bo',Freq,Db,'k')
plt.grid(True)
plt.show()
