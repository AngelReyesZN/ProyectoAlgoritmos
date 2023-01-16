import math
import numpy as np
from matplotlib import pyplot as plt

#-----------------------------------------------------------------------------------------
### METODO MEDIA MOVIL SIN DATOS ACTUALIZADOS - NOVIEMBRE-DICIEMBRE #############################
#-----------------------------------------------------------------------------------------





dia=[31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,
     54,55,56,57,58,59,60,61]

casos=[177731,177750,177760,177769,177815,177864,177909,177943,177980,177998,178012,
       178082,178133,178205,178288,178360,178384,178402,178543,178694,178833,178979,179099,
       179120,179131,179315,179422,179581,179703,179794,179807]


casosr=[177731,177750,177760,177769,177815,177864,177909,177943,177980,177998,178012,
       178082,178133,178205,178288,178360,178384,178402,178543,178694,178833,178979,179099,
       179120,179131,179315,179422,179581,179703,179794,179807]


n=177696


diap=[26,27,28,29,30]
casosp=[177597,177603,177636,177669,177696]


casosdic=[]

res=[3]



for j in range(0,31):
    
    for i in range(0,4):
            
        res.append(casosp[i+1]-casosp[i])
        promedio=np.mean(res)
    
    if(j==0):
        casosdicentero=n+promedio
        casosdic.append(n+promedio)
        promedio=0
        casosp.pop(0)
        casosp.append(casosdicentero)
        res.clear()
        
    else:
        casosdicentero=casosdicentero+promedio
        casosdic.append(casosdicentero)
        promedio=0
        casosp.pop(0)
        casosp.append(casosdicentero)
        res.clear()




#Creación de la grafica------------
plt.figure(figsize=[50,50])
plt.title("Casos COVID-19 Queretaro - Diciembre 2023")
plt.scatter(dia,casosr,s=20, c='blueviolet')
plt.scatter(dia,casosdic,s=20, c='orange')
plt.legend(["Casos reales", "Casos estimados"], loc ="lower right")
plt.plot(dia,casosr, color="blueviolet")
plt.plot(dia,casosdic, color="orange")
plt.yticks(range(177700,179850,100)) #177731-179807
plt.grid("on")
ax=plt.gca()
ax.set_xlabel("Dias (Diciembre)")
ax.set_ylabel("Casos Acumulados")
plt.show()
