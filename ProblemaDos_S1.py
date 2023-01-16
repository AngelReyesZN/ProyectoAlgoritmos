#Dos números enteros positivos A y B son números amigos si la suma de los divisores propios de A es igual a B y la suma de los divisores propios
#de B es igual a A. Los divisores propios de un número incluyen la unidad pero no el propio número.

# o    Un ejemplo de números amigos son los números 220 y 284.
# 
# o    Los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110.
# 
# o    La suma de los divisores propios de 220 da como resultado 284
# 
# o    Los divisores propios de 284 son 1, 2, 4, 71 y 142.
# 
# o    La suma de los divisores propios de 284 da como resultado 220.
# 
# o    Por lo tanto 220 y 284 son amigos.

divisores=[]
numerouno=input("Introduce el primer número: ")
numerouno=int(numerouno)

numerodos=input("Introduce el primer número: ")
numerodos=int(numerodos)

#numerodos=input("Introduce el segundo número: ")
#numerodos=int(numerodos)
r=0
residuo=0
for i in range(1, numerouno):
    
    
    numerounod=numerouno/i
    numerouno=float(numerouno)
    residuo=float(residuo)
    r=float(r)
    numeroaux=numerounod
    numeroaux=int(numeroaux)
    r=i*numeroaux
    residuo=numerouno-r
    #print("Cuando el divisor es: ", i, " el resultado es: ", numerounod, "y el residuo es: ", residuo)
    if residuo==0:
         #print("Cuando el divisor es: ", i, " el resultado es: ", numerounod, "y el residuo es: ", residuo)
         divisores.append(i)
         #print("La suma de los divisores es: ", sum(divisores))
         
         sumadiv=sum(divisores)
         
         if sumadiv==numerodos:
             print("Felicidades son numeros amigos")
         
             break
            
if sumadiv!=numerodos:
    print("No son numero amigos")
       


########################### Parte del segundo número ################








