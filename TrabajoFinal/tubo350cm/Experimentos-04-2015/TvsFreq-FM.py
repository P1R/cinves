import numpy as np
import matplotlib.pyplot as plt
#la frecuencia de la modulada FM es de 50 hz en todas las variaciones de la portadora
Freq=np.array([20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260]);
DeltaTemp=np.array([0.5,1.2,3.2,4.1,2.3,2.0,1.8,0.8,0.2,1.2,2.3,4.1,8.5,3.4,0.1,2.6,3.8,3.3,1.1,0.5,1.7,3.4,5.0,4.4,1.9])
TempT1=np.array([20.8,20.3,18.8,17.9,23.2,22.8,22.7,22.9,21.2,20.3,19.9,19.2,17.1,19.8,22.1,22.0,23.6,24.0,22.6,21.6,20.8,19.9,18.9,18.8,20.4])
TempT2=np.array([21.3,21.5,22.0,22.0,20.9,20.8,20.9,22.1,21.4,21.5,22.2,23.3,25.6,23.2,22.2,19.4,19.8,20.7,21.5,22.1,22.5,23.3,23.9,23.2,22.3])
TempAmb=np.array([21.0,21.0,21.0,21.0,21.1,21.3,21.3,21.4,20.9,21.0,21.1,21.4,21.5,21.6,21.8,19.3,20.0,20.6,20.8,21.2,21.2,21.2,21.2,21.3,21.3])

plt.xlabel('Frecuencia')
plt.ylabel('Temperatura')
plt.title('Temperatura vs Frecuencia modulada en FM')
#for i in range(len(Freq)):
#	plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 280, 0, 30])
plt.plot(Freq,TempT1,'bo',Freq,TempT1,'k')
plt.plot(Freq,TempT2,'r^',Freq,TempT2,'r')
plt.plot(Freq,DeltaTemp,'ko',Freq,DeltaTemp,'k')
plt.plot(Freq,TempAmb,'yo',Freq,TempAmb,'y')
plt.grid(True)
plt.show()

