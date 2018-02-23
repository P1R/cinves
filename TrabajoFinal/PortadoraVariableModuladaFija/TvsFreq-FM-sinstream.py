import numpy as np
import matplotlib.pyplot as plt
'''
Experimento con 0.5 volts de amplitud y medicion tomada cada 2 minutos *sin streaming*
la frecuencia de la modulada FM es de 50 hz en todas las variaciones de la portadora
'''
Freq=np.array([30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260]);
DeltaTemp=np.array([1.6,4.5,10.2,3.7,2.5,2.1,0.9,0.3,1.3,2.4,4.7,11.48,3.5,1.4,3.2,4.5,3.8,1.4,0.6,2.1,4.4,6.5,6.4,1.8])
TempT1=np.array([20.6,19.3,16.5,23.8,23.5,23.4,24.2,23.3,22.5,21.8,20.8,17.7,19.0,21.8,23.9,25.0,25.7,24.3,23.0,22.1,21.0,20.0,19.8,21.7])
TempT2=np.array([22.2,23.8,26.7,20.9,21.0,21.3,23.3,23.6,23.8,24.2,25.5,29.5,22.5,20.4,20.2,20.5,21.9,22.9,23.6,24.2,25.4,26.5,26.2,23.5])
TempAmb=np.array([21.7,21.7,21.8,22.4,22.5,22.4,22.5,23.4,23.2,22.8,22.9,22.7,20.8,21.1,21.8,22.0,22.4,22.8,23.0,22.8,22.7,22.8,22.9,22.8])

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

