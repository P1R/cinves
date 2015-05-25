import numpy as np
import matplotlib.pyplot as plt

Freq=np.array([20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260]);
DeltaTemp=np.array([0.5,1.3,3.2,6.5,2.3,1.9,1.7,1,0,0.9,1.9,3.4,7.5,5.4,0.1,2.4,3.8,3.3,1.0,0.7,2.1,3.9,5.7,4.5,2.1])
TempT1=np.array([17.5,17.0,15.7,13.3,20.5,20.2,20.0,19.8,19.5,18.8,18.2,17.5,15.3,16.0,20.1,22.2,23.3,23.7,22.2,21.1,20.4,19.4,18.2,16.6,18.6])
TempT2=np.array([18.0,18.3,18.9,19.8,18.2,18.3,18.3,18.8,19.5,19.7,20.1,20.9,22.8,21.4,20.0,19.8,19.5,20.4,21.2,21.8,22.5,23.3,23.9,21.1,20.7])
TempAmb=np.array([17.8,17.9,17.9,18.1,18.2,18.8,18.8,18.0,18.6,19.0,19.0,19.2,19.3,19.6,19.7,20.2,20.5,20.6,21.0,20.9,21.0,21.1,21.1,19.7,20.0])

plt.xlabel('Frecuencia')
plt.ylabel('Temperatura')
plt.title('Temperatura vs Frecuencia sin MODULACION')
#for i in range(len(Freq)):
#	plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 280, 0, 30])
plt.plot(Freq,TempT1,'bo',Freq,TempT1,'k')
plt.plot(Freq,TempT2,'r^',Freq,TempT2,'r')
plt.plot(Freq,DeltaTemp,'ko',Freq,DeltaTemp,'k')
plt.plot(Freq,TempAmb,'yo',Freq,TempAmb,'y')
plt.grid(True)
plt.show()

