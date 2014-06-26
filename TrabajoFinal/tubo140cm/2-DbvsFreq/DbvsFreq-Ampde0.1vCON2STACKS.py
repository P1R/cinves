#!/usr/bin/env	python2.7
import numpy as np
import matplotlib.pyplot as plt

Freq=np.array([40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400])
Db=np.array([70,72.7,77,81.1,85.4,90.1,95.6,101.7,102.6,101.1,99.6,99.4,99.1,100.2,101.6,103.2,105.6,107.5,110.6,112.8,113.3,113.2,113,112.7,112.2,112.3,112.5,112.8,113.1,114,115.2,116.9,118.4,118.1,116.2,114.4,112.1])
plt.xlabel('Frecuencia')
plt.ylabel('Decibel')
plt.title('DecibelvsFreq a 0.1volts + 2 stacks')
#for i in range(len(Freq)):
#	plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 430, 50, 130])
plt.plot(Freq,Db,'bo',Freq,Db,'k')
plt.grid(True)
plt.show()
