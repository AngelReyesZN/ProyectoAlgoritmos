
numeros=[]

n=input("Introduce el numero a sacar el factorial: ")
n=int(n)

s=n

for i in range(1,n):
    s=s*(n-1)
    n=n-1
    
print("El resultado es: " ,s)