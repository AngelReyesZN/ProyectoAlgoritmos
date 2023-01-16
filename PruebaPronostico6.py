
import math
import numpy as np
from matplotlib import pyplot as plt







diap=[1,31]
casosXdiapNov=[177343,177696]


diaNov=[32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61]

casos=[177731,177750,177760,177769,177815,177864,177909,177943,177980,177998,178012,
       178082,178133,178205,178288,178360,178384,178402,178543,178694,178833,178979,179099,
       179120,179131,179315,179422,179581,179703,179794]




x1=diap[0]


y1=casosXdiapNov[0]
x2=diap[1]
y2=casosXdiapNov[1]
x=32


for i in range(0,30):
    
    
    
    x1=diap[0]
    y1=casosXdiapNov[0]
    x2=diap[1]
    y2=casosXdiapNov[1]
    
    res=(((x-x1)*(y2-y1))/(x2-x1))+y1
    
    casosXdiapNov.append(res)
    diap.append(x)
    if (x>=31):
        y=x-31
    print("El valor estimado para", y, " es", res)
    x=x+1


diap.pop(0)
casosXdiapNov.pop(0)


#Creación de la grafica------------
plt.figure(figsize=[50,50])
plt.title("Casos COVID-19 Queretaro - Diciembre 2023")
plt.scatter(diaNov,casos,s=20, c='blueviolet')
plt.scatter(diap,casosXdiapNov,s=20, c='orange')
plt.legend(["Casos reales", "Casos estimados"], loc ="lower right")
plt.plot(diap,casosXdiapNov, color="orange")
plt.plot(diaNov,casos, color="blueviolet")
plt.yticks(range(177720,180000,100)) 
plt.grid("on")
ax=plt.gca()
ax.set_xlabel("Dias (Noviembre)")
ax.set_ylabel("Casos Acumulados")
plt.show()
