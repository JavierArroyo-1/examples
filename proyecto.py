import serial
import collections
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
arduino = serial.Serial("COM5", 9600)



def getSerialData(self,Samples,arduino,lines,lineValueText,lineLabel):
  Value = float(arduino.readline().strip())
  data.append(Value)
  lines.set_data(range(Samples),data)
  lineValueText.set_text(lineLabel+' - '+ str(round(Value,2)))
  
Samples=100
data= collections.deque([0]*Samples, maxlen=Samples)

xmin = 0
xmax = Samples
ymin = 0
ymax = 6

fig = plt.figure(figsize=(13,6))
ax = plt.axes(xlim=(xmin,xmax), ylim=(ymin,ymax))
plt.title("Tiempo real del sensor")
ax.set_xlabel("Samples")
ax.set_ylabel("Voltaje")

lineLabel = 'Temperatura'
lines = ax.plot([],[], label=lineLabel)[0]
lineValueText = ax.text(0.85, 0.95, '', transform=ax.transAxes)

anim = animation.FuncAnimation(fig, getSerialData, fargs = (Samples, arduino, lines, lineValueText, lineLabel))
plt.show()

arduino.close()





