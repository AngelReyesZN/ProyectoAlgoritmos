import math
import numpy as np
from matplotlib import pyplot as plt


#-----------------------------------------------------------------------------------------
### METODO INTERPOLACIÓN LINEAL CON ULTIMOS DOS PUNTOS - OCTUBRE-NOVIEMBRE #############################
#-----------------------------------------------------------------------------------------



diap=[30,31]
casosXdiapNov=[177325,177336]


diaNov=[32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61]

casos=[177343,177353,177364,177370,177371,177375,177386,177398,177412,177430,177449,177452,177454,177471,177486,
       177493,177503,177505,177507,177508,177510,177529,177556,177572,177593,177596,177602,177635,177667,177694]




x1=diap[0]


y1=casosXdiapNov[0]
x2=diap[1]
y2=casosXdiapNov[1]
x=32


for i in range(0,30):
    
    
    
    x1=diap[i]
    y1=casosXdiapNov[i]
    x2=diap[i+1]
    y2=casosXdiapNov[i+1]
    
    res=(((x-x1)*(y2-y1))/(x2-x1))+y1
    casosXdiapNov.append(res)
    diap.append(x)
    if (x>=31):
        y=x-31
    print("El valor estimado para", y, " es", res)
    x=x+1


#Creación de la grafica------------
plt.figure(figsize=[50,50])
plt.title("Casos COVID-19 Queretaro - Diciembre 2023")
plt.scatter(diaNov,casos,s=20, c='blueviolet')
plt.scatter(diap,casosXdiapNov,s=20, c='orange')
plt.legend(["Casos reales", "Casos estimados"], loc ="lower right")
plt.plot(diaNov,casos, color="blueviolet")
plt.plot(diap,casosXdiapNov, color="orange")
plt.yticks(range(177300,177700,100)) 
plt.grid("on")
ax=plt.gca()
ax.set_xlabel("Dias (Noviembre)")
ax.set_ylabel("Casos Acumulados")
plt.show()




