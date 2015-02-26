import numpy as np
import matplotlib.pyplot as plt
#la frecuencia de la modulada FM es de 50 hz en todas las variaciones de la portadora
Freq=np.array([20,30,40,50,60,70,80,90,100,110,120,130,140,150,160]);
DeltaTemp=np.array([0.5,1.2,3.2,4.1,2.3,2.0,1.8,0.8,0.2,1.2,2.3,4.1,8.5,3.4,0.1])
TempT1=np.array([20.8,20.3,18.8,17.9,23.2,22.8,22.7,22.9,21.2,20.3,19.9,19.2,17.1,19.8,22.1])
TempT2=np.array([21.3,21.5,22.0,22.0,20.9,20.8,20.9,22.1,21.4,21.5,22.2,23.3,25.6,23.2,22.2])
TempAmb=np.array([21.0,21.0,21.0,21.0,21.1,21.3,21.3,21.4,20.9,21.0,21.1,21.4,21.5,21.6,21.8])

plt.xlabel('Frecuencia')
plt.ylabel('Temperatura')
plt.title('Temperatura vs Frecuencia modulada en FM')
#for i in range(len(Freq)):
#	plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 200, 0, 30])
plt.plot(Freq,TempT1,'bo',Freq,TempT1,'k')
plt.plot(Freq,TempT2,'r^',Freq,TempT2,'r')
plt.plot(Freq,DeltaTemp,'ko',Freq,DeltaTemp,'k')
plt.plot(Freq,TempAmb,'yo',Freq,TempAmb,'y')
plt.grid(True)
plt.show()

