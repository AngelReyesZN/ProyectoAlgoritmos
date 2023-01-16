
import random 

#primero definir puntos  a utilizar

n=10000

#suponer que tenemos un radio 1

radio=1
#necesitacmos el centro del circulo

a,b=0,0

#vamos a necesitar las coordenadas para los puntos alrededor del centro del circulo

x_negativa=a-radio
x_positiva=a+radio


y_negativa=b-radio
y_positiva=b+radio


contador=0

for i in range(n):
    x=random.uniform(x_negativa,x_positiva)
    y=random.uniform(y_negativa,y_positiva)
    
    
    #cayo dentro o fuera
    if x*x+y*y<=1:
        contador=contador+1
print((contador/float(n)*4))





















