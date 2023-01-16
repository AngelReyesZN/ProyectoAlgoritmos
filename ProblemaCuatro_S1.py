# Programa que lea dos números enteros positivos N y M y muestre los múltiplos de N que hay desde 1 hasta M. Por ejemplo si N = 4 y M = 500 el
#programa mostrará los múltiplos de 4 desde 1 hasta 500.El valor de N deberá ser menor que el valor de M. Si no se introducen valores
#válidos para N o M se mostrará el mensaje correspondiente y se vuelven a pedir.


n=input("Introduce el primer numero: ")
n=int(n)

m=input("Introduce el primer numero: ")
m=int(m)


if n>m:
    print("Error, vuelve a intentarlo")
    n=input("Introduce el primer numero: ")
    n=int(n)

    m=input("Introduce el primer numero: ")
    m=int(m)



for i in range(1, m+1):
  dividendo=i
  divisor=n
  residuo=0
  cociente=dividendo/divisor
  cociente=int(cociente)
  residuo=(cociente*divisor)-dividendo 
  #print(cociente)
  if residuo==0:
      print(i)
    
  
    
