# Programa Java que lee una temperatura expresada en grados centígrados y la convierte a grados kelvin.
#El proceso de leer grados centígrados se debe repetir mientras que se responda ‘S’ a la pregunta: Repetir proceso? (S/N).
#Para hacer la conversión de grados Centígrados a grados Kelvin hay que utilizar la fórmula: ºK = ºC + 273


res=input("¿Deseas iniciar el conversor?")




while res=="S":

    gradosC=input("Introduce los grados Centígrados: ")
    gradosC=int(gradosC)
    
    gradosK=gradosC+273
    print("/////////////////////////////////////////////////")
    print("La temperatura en grados Kelvin es de: ", gradosK)
    print("/////////////////////////////////////////////////")
    res=input("¿Deseas repetir el proceso?")

if res=="N":
    print("Has salido del conversor")
    

if res!= "S" or "N":
    res=input("¿Deseas iniciar el conversor?")