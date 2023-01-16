#Programa que pida que se introduzca por teclado el valor de un número entero N y muestre los números desde N hasta 1 ambos incluidos. Se debe resolver este ejercicio de tres
# formas distintas: utilizando la estructura repetitiva while, utilizando la estructura repetitiva do .. while y utilizando la estructura repetitiva for.

############ 1 #########
# numero=input("Introduce un número: ")
# numero=int(numero)
# numerof=numero 
# 
# 
# i=2
# 
# print(numero) 
# while i <= numero:
#     
#     
#     numerof -= 1
#     print(numerof)
#     i += 1

############ 2 #########



numero=input("Introduce un número: ")
numero=int(numero)
numerof=numero 

print(numero) 
for i in range(1, numero):

    numerof -=1
    print(numerof)
    i += 1
    
    
    
    