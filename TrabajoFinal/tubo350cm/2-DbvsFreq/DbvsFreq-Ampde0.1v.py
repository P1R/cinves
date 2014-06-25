#!/usr/bin/env	python2.7
import numpy as np
import matplotlib.pyplot as plt

Freq=np.array([20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320])
Db=np.array([90
	,96.4
	,104.3
	,116
	,108.5
	,106.6
	,108.4
	,114.5
	,120
	,112.8
	,111.2
	,113.6
	,120.3
	,120.5
	,115.9
	,115.2
	,118
	,123.6
	,122
	,118.6
	,118.6
	,121.3
	,124.4
	,123.5
	,121.9
	,121.7
	,122.4
	,123.8
	,125.5
	,123.9
	,121])
plt.xlabel('Frecuencia')
plt.ylabel('Decibel')
plt.title('DecibelvsFreq a 0.1volts')
#for i in range(len(Freq)):
#		plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 330, 50, 130])
plt.plot(Freq,Db,'bo',Freq,Db,'k')
plt.grid(True)
plt.show()
