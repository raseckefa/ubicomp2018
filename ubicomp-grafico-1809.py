import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import datetime
import serial
from matplotlib import style

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# VALIDA JAVINO
def getdata(d, t):
    try:
		r = 0
		x = int(d[4:6], 16)
		# VALIDA PREFIXO FFFE
		if (d[:4] != 'fffe'):
			return 0
		# VALIDA QUANTIDADE DE CARACTERES	
		elif (int(len(d[6:].strip())) != x):
			return 0
		# RECUPERA DADO DE TEMPERATURA	
		elif (t == 'temp'):
			r = d[6:].split('|')[0]
			return int(float(r.split('temp=')[1].strip()))
		# RECUOERA DADO DE LUMINOSIDADE	
		elif (t == 'lumin'):
			r = d[6:].split('|')[1]
			return int(float(r.split('lumin=')[1].strip())) 	
		else:
			return r
    except:
			return 0

# GRAFICO ANIMADO
def animate(i):
	# RECUPERA DADO DO ARDUINO
	d = ser.readline()
	if (d.strip() != ''):
		# RECUPERA TEMPERATURA E LUMINOSIDADE
		temp = getdata(d, 'temp')
		lumin = getdata(d, 'lumin')

		if ((temp != 0) and (lumin != 0)):
			# RECUPERA HORA MIN E SEGUNDO ATUAL
			now = datetime.datetime.now().strftime('%H:%M:%S')
			x.append(str(now))
			yT.append(temp)
			yL.append(lumin)				
			ax1.clear()
			# REMOVE PRIMEIRO VELOR DO VETOR
			# O GRAFICO NAO DEVE EXIBIR MAIS QUE 50 REGISTROS
			if (len(x) > 50):
				x.pop(0)
				yT.pop(0)
				yL.pop(0)

			ax1.plot(x, yT, 'go-', linewidth=2, markersize=6, color='blue')
			ax1.plot(x, yL, 'go-', linewidth=2, markersize=6, color='red')
			# DESENHA LEGENDA
			red_patch = mpatches.Patch(color='red', label='Luminosidade ('+str(lumin)+' de 0 a 102)')
			blue_patch = mpatches.Patch(color='blue', label='Temperatura ('+str(temp)+' C)')
			plt.legend(handles=[red_patch, blue_patch])
			# AJUSTA LAYOUT DO GRAFICO
			plt.xticks(rotation='vertical')
			plt.subplots_adjust(bottom=0.3)
# INICIA VARIAVEIS
x = [0]
yT = [0]
yL = [0]	
# CONECTA NA PORTA COM APROPRIADA
ser = serial.Serial('COM7', 9600, timeout=0)
# INICIA INTERVALO DE ATUALIZACAO DO GRAFICO
ani = animation.FuncAnimation(fig, animate, interval=500)	
plt.show()






































