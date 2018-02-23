import numpy as np
import matplotlib.pyplot as plt
'''

La Frecuencia Base es de 50 Hz y las variaciones en frecuencia de rate de 30 a 200
este ejemplo es con un pawn de 100% en AM.

para este experimento los valores son: 
	tiempo de medicion: 2 minutos
	voltaje de generador: 0.3 volts
	tubo de prueba: cobre 350 cm
	SIN STREAMING.
'''
Freq=np.array([30,40,50,60,70,80,90,100,200])
DeltaTemp=np.array([0.8,0.3,0.7,0.7,1.2,1.5,2.0,2.5,1.7])
TempT1=np.array([21.5,21.9,21.9,22.0,22.0,21.8,21.6,21.3,21.8])
TempT2=np.array([22.3,22.2,22.6,22.7,23.2,23.3,23.6,23.8,23.5])
TempAmb=np.array([21.9,21.9,22.1,22.2,22.6,22.6,22.6,22.6,22.6])

plt.xlabel('Rate')
plt.ylabel('Temperatura')
plt.title('Temperatura vs Rate en AM con pawn de 100%')
#for i in range(len(Freq)):
#	plt.text(Freq[i],Db[i], r'$Freq=%f, \ Db=%f$' % (Freq[i], Db[i]))
plt.axis([0, 220, 0, 30])
plt.plot(Freq,TempT1,'bo',Freq,TempT1,'k')
plt.plot(Freq,TempT2,'r^',Freq,TempT2,'r')
plt.plot(Freq,DeltaTemp,'ko',Freq,DeltaTemp,'k')
plt.plot(Freq,TempAmb,'yo',Freq,TempAmb,'y')
plt.grid(True)
plt.show()

