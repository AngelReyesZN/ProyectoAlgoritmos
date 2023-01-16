import numpy as np
from matplotlib import pyplot as plt

#-----------------------------------------------------------------------------------------
### METODO ECUACION DE COEFICIENTE DE CORRELACIÓN LINEAL - OCTUBRE-NOVIEMBRE #############
#-----------------------------------------------------------------------------------------



diaoct=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31] # Dias de octubre 

casosoct=[177143,177144,177159,177167,177182,177194,177200,177206,177209,177212,177217,177225,177233,
          177239,177240,177240,177244,177254,177257,177265,177270,177272,177278,177285,177300,177310,
          177316,177320,177323,177325,177336] # Casos de contagios reales octubre 1-31

casosp=[] # Lista donde se agregan los casos pronosticados

dianov=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30] # Dias de noviembre usados para
# representar el eje x

casosnov=[177343,177353,177364,177370,177371,177375,177386,177398,177412,177430,177449,177452,177454,177471,177486,
       177493,177503,177505,177507,177508,177510,177529,177556,177572,177593,177596,177602,177635,177667,177694]
# Casos reales de noviembre usados solamente para graficar 

# x = dias
# y = casos reales de octubre




# Calculo realizado mediante las siguientes formulas:
# y = ax + b  
    
# a = n Σxy - Σx Σy / n Σx² - Σ(x)²

# b = Σy - a Σx / n


cuadrado=[] # Se crea lista donde se iran agregando los cuadrados de x por cada dia 
xXy=[] # Lista donde se agregara el resultado de x*y por cada dia 

sumdias=sum(diaoct) # Sumatoria de x

sumcasos=sum(casosoct) # Sumatoria de y



for i in range(0,31): # Proceso que se repetira 31 veces ya que son los dias de octubre
    
    cuadrado.append(diaoct[i]*diaoct[i]) # Se agrega a la lista cuadrado el resultado de x² por cada dia
    xXy.append(diaoct[i]*casosoct[i])  # Se agrega a la lista xXy el resultado de x*y por cada dia


    
sumcuadrados=sum(cuadrado)    
sumxXy=sum(xXy)    
n=len(diaoct)

a=((n*sumxXy)-(sumdias*sumcasos))/((n*sumcuadrados)-(sumdias*sumdias))

b=(sumcasos-(a*sumdias))/n

for j in range(31,61):
    x=float(j)
    y=a*x+b
    casosp.append(y)
    
   
   


#Creación de la grafica------------
plt.figure(figsize=[50,50])
plt.title("Casos COVID-19 Queretaro - Noviembre 2022")
plt.scatter(dianov,casosnov,s=20, c='blueviolet')
plt.scatter(dianov,casosp,s=20, c='orange')
plt.legend(["Casos reales", "Casos estimados"], loc ="lower right")
plt.plot(dianov,casosp, color="orange")
plt.plot(dianov,casosnov, color="blueviolet")
plt.yticks(range(177300,177700,100)) 
plt.grid("on")
ax=plt.gca()
ax.set_xlabel("Dias (Noviembre)")
ax.set_ylabel("Casos Acumulados")
plt.show()



    
    
    
    
    
    