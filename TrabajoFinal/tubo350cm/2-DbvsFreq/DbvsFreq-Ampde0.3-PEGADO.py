#!/usr/bin/env	python2.7
import numpy as np
import matplotlib.pyplot as plt

Freq=np.array([30,40,45,50,55,60,65,70,80,90,95,100,105,110,125,130,140,145,150,160,170,180,190,195,200,210,220,230,240,245,250,260,270,280,290,295,300,305,310,320,325,330,335,340,345,350,355,360])
Db=np.array([70,77,86.7,97.2,90.4,87.7,87.2,88,91.9,99.9,106.8,107.4,102.8,100.4,100.2,100.3,111.9,116.2,113.4,108.2,108.4,111.8,118.7,119.5,117.2,113.8,114.8,118.1,121.7,121.6,121,119.9,120.4,121.1,122.5,123.5,124.4,124.7,124.1,121,120,119.7,120.2,122.1,126.2,126.9,126.5,123.3])
plt.xlabel('Frecuencia')
plt.ylabel('Decibel')
plt.title('DecibelvsFreq a 0.3volts PEGADO')
#for i in range(len(Freq)):
#		plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 370, 50, 130])
plt.plot(Freq,Db,'bo',Freq,Db,'k')
plt.grid(True)
plt.show()
