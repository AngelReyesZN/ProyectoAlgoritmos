import numpy as np # Libreria utlizada para poder utilizar ciertas funciones propias de numpy
import matplotlib.pyplot  as plt # Libreria utlizada para poder graficar nuestros datos 

# Proyecto Final - Reyes Ventura Luis Angel - 307060
#-----------------------------------------------------------------------------------------
### METODO MEDIA MOVIL CON DATOS ACTUALIZADOS - NOVIEMBRE-DICIEMBRE ######################
#-----------------------------------------------------------------------------------------


dia=np.array([31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,
     54,55,56,57,58,59,60,61])# Días de Diciembre empezando de 31-61 ya que se toma en cuenta los dias de noviembre desde el 26-30.

casos=[177731,177750,177760,177769,177815,177864,177909,177943,177980,177998,178012,
       178082,178133,178205,178288,178360,178384,178402,178543,178694,178833,178979,179099, # Casos reales movibles, que se van
       179120,179131,179315,179422,179581,179703,179794,179807]  # eliminando de acuerdo lo vaya necesitando el programa. 


casosr=np.array([177731,177750,177760,177769,177815,177864,177909,177943,177980,177998,178012,
       178082,178133,178205,178288,178360,178384,178402,178543,178694,178833,178979,179099, # Casos reales fijos, se utilizan 
       179120,179131,179315,179422,179581,179703,179794,179807])# unicamente para graficar los datos reales de diciembre.



diap=[25,26,27,28,29,30] # Ultimos dias 5 dias de noviembre 26-30.
casosp=[177594,177597,177603,177636,177669,177696] # Ultimos cifras de contagios de noviembre 26-30.

casosdic=[] # Lista donde se agregan los casos pronosticados.

res=[] # Lista donde se almacenan las ultimas 5 diferencias de los ultimos 5 dias.



for j in range(0,31): # Indica que el proceso  se repetira 31  veces ya que diciembre contiene 31 días. 
    
    for i in range(0,5): # Proceso que realiza las restas entre los 5 ultimos contagios
        # reales uno por uno y al final los promedia.
            
        res.append(casosp[i+1]-casosp[i]) # Agrega a la lista resta las ultimas 5 diferencias 
        promedio=np.mean(res) # Promedia las diferencias de las ultimas 5 diferencias. 
           
    casosdic.append(int(casosp[5]+promedio)) # Se agrega a la lista de casos pronosticados el resultado
    # de ultima cifra real conocida mas el promedio de los las ultimas 5 cifras de contagios.
    
    diad=j+1 # Ajuste para imprimir el dia.
    print("Para el dia " ,diad ," de diciembre, los contagios serán de: " , casosdic[j]) # Imprime el dia
    # y los casos pronosticados para ese dia.
    
    promedio=0 # Se iguala el promedio a cero para que no se acumulen promedio anteriores.
    
    casosp.pop(0) # Se elimina el primer valor de la lista que se utliza para realizar las diferencias.
    
    casosp.append(casos[0]) # Se agrega a esa lista el primer valor de la lista de casos reales ( simulando
    # una actualización diaria ).
    
    casos.pop(0) # Se elimina el primer caso de la lista de casos reales ya que ya se utlizo en la linea de arriba.
    
    res.clear() # Se eliminan todos los valores de la lista de diferencia para que no se acumulen las
    # diferencias de días anteriores ya que solo se ocupan 5 valores.
     
        

#-----------------------------------------------------------------------------------------
### COEFICIENTE DE CORRELACION ###########################################################
#-----------------------------------------------------------------------------------------

# x = reales
# y = pronosticos
 
# Calculo de r segun la formula: Σ(x - x̄)*(y - ) / √(Σ(x - x̄)² Σ(y - )²).
 
 
promediox=np.mean(casosr) # Se realiza el promedio de x.
promedioy=np.mean(casosdic) # Se realiza el promedio de y.


xmenospromedio=[] # Se crea una lista para agregar todas las x - x̄.
ymenospromedio=[] # Se crea una lista para agregar todas las y - .

xmenospromedio2=[] # Se crea una lista para agregar todas las (x - x̄)².
ymenospromedio2=[] # Se crea una lista para agregar todas las (y - )².

xpory=[] # Se crea una lista para agregar todas las (x - x̄)*(y - ).

for i in range(0,31): # Se repite este proceso 31 veces ya que son los dias que contiene diciembre.
    
    xmenospromedio.append(casosr[i]-promediox) # Se agrega a la lista xmenospromedio el resultado de
    # la operacion de (x - x̄) por dia.
    
    ymenospromedio.append(casosdic[i]-promedioy) # Se agrega a la lista ymenospromedio el resultado de 
    # la operacion de (y - ) por dia.
    

    xmenospromedio2.append(xmenospromedio[i]*xmenospromedio[i]) # Se agrega a la lista xmenospromedio2
    #  el resultado de la operacion de (x - x̄)² por dia.
    
    ymenospromedio2.append(ymenospromedio[i]*ymenospromedio[i]) # Se agrega a la lista ymenospromedio2
    #  el resultado de la operacion de (y - )² por dia.

    xpory.append(xmenospromedio[i]*ymenospromedio[i]) # Se agrega a la lista xpory
    #  el resultado de la operacion de (x - x̄)*(y - ) por dia.


sumax=sum(xmenospromedio2) # Se realiza la sumatoria de todos los resultados diarios de (x - x̄)².
sumy=sum(ymenospromedio2) # Se realiza la sumatoria de todos los resultados diarios de (y - )².
suma3=sum(xpory) # Se realiza la sumatoria de todos los resultados diarios de (x - x̄)*(y - ).


r=suma3/(np.sqrt(sumax)*np.sqrt(sumy)) # Al final solo se aplica la formula en conjunto. 

print("El coeficiente de correlacion es de: ", r) # Se imprime R.



casosx=np.array([casosdic])  # Se aplica numpy a esta lista para poder aplicar la función CORRCOEF.



r2=np.corrcoef(casosr,casosx) # Función utilizada para comprobar el calculo de r.

print("El coeficiente de correlación calculado con la función CORRCOEF es de: ",r2) # Se imprime R en forma
# de matriz.



#-----------------------------------------------------------------------------------------
### CREACIÓN DE LA GRÁFICA ###############################################################
#-----------------------------------------------------------------------------------------


plt.figure(figsize=[60,60]) # Indica el tamaño de la gráfica.

plt.title("Casos COVID-19 Queretaro - Diciembre 2023") # Se inserta un titulo a la gráfica.

plt.scatter(dia,casosr,s=20, c='blueviolet') # Se grafican los casos reales con puntos violetas (s = size, c = color).

plt.scatter(dia,casosdic,s=20, c='orange') # Se grafican los casos pronosticados con puntos naranjas (s = size, c = color).

plt.legend(["Casos reales", "Casos estimados"], loc ="lower right") # Se inserta la simbologia de la grafica.
# (#Titulo 1, Titulo 2, location)

plt.plot(dia,casosr, color="blueviolet") # Se grafican los casos reales con una linea violeta.

plt.plot(dia,casosdic, color="orange") # Se grafican los casos pronosticados con una linea naranja.

plt.yticks(range(177700,179950,100)) # Usado para establecer limites de Y y el valor de separacion entre valores.

plt.grid("on") # Se cuadricula el espacio de la gráfica.

ax=plt.gca() # Se utiliza para obtener las valores de los ejes.

ax.set_xlabel("Dias (Diciembre)") # Se inserta un titulo para el eje x.

ax.set_ylabel("Casos Acumulados") # Se inserta un titulo para el eje y.

plt.show() # Finalmente con este comando se muestra la gráfica.




















