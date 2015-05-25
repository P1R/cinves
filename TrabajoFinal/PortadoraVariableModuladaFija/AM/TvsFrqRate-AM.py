import numpy as np
import matplotlib.pyplot as plt
'''

La Frecuencia Base es de 50 Hz y las variaciones en frecuencia de rate de 30 a 200
este ejemplo es con un pawn de 50% en AM.

para este experimento los valores son: 
	tiempo de medicion: 2 minutos
	voltaje de generador: 0.3 volts
	tubo de prueba: cobre 350 cm
	SIN STREAMING.
'''
Freq=np.array([20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180]);
DeltaTemp=np.array([0.4,0.7,1,1.1,0.4,0.7,0.8,0.8,0.2,0.7,1.2,1.8,3.7,0.9,0.1,0.1,1.8])
TempT1=np.array([18.8,18.6,18.7,18.8,18.4,18.9,19.1,20.2,19.9,19.8,20.2,20.1,19.1,20.4,21.1,21.6,22.5])
TempT2=np.array([19.2,19.3,19.7,19.9,18.0,18.2,18.3,19.4,20.1,20.5,21.4,21.9,22.8,21.3,21.0,20.9,20.7])
TempAmb=np.array([18.9,19.0,19.2,19.5,18.4,18.6,18.6,19.0,19.8,20.3,20.9,20.5,20.6,20.8,20.8,20.9,21.0])

plt.xlabel('Rate')
plt.ylabel('Temperatura')
plt.title('Temperatura vs Rate en AM con pawn de 50%')
#for i in range(len(Freq)):
#	plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 200, 0, 30])
plt.plot(Freq,TempT1,'bo',Freq,TempT1,'k')
plt.plot(Freq,TempT2,'r^',Freq,TempT2,'r')
plt.plot(Freq,DeltaTemp,'ko',Freq,DeltaTemp,'k')
plt.plot(Freq,TempAmb,'yo',Freq,TempAmb,'y')
plt.grid(True)
plt.show()

