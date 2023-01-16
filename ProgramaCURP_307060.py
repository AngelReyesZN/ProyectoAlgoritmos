
vocales=['A','E','I','O','U']
estado = None	
estados = { 
    '':'', 'CAMPECHE':'CC', 'QUERETARO':'QT',
		}
listacurp9=[]
espacioblanco=[' ']

palabrasGroseras=['PENE','CACA','PUTO','PUTA','PITO','POPO','PIPI','MECO','CULO','COLA','TETA','SEXO']





primerapellido=input("Ingresa tu primer apellido: ")

# primerapellido.split()
primerapellido=list(primerapellido)

for k in range(len(primerapellido)):
    
    
        if(primerapellido[k]=='Ñ'):
            
            
            primerapellido[k]='X'
        
            continue





for i in range(len(primerapellido)):
    
    
        if(primerapellido[i] in vocales and i>0):
            
            
            listacurp=primerapellido[0], primerapellido[i]
            break
        
for j in range(len(primerapellido)):
    
    
        if(primerapellido[j] not in vocales and j>0):
            
            
            listacurp9.append(primerapellido[j])
            
            break       
        
                
    

segundoapellido=input("Ingresa tu segundo apellido: ")
segundoapellido=list(segundoapellido)


for j in range(len(segundoapellido)):
    
    
        if(segundoapellido[j]=='Ñ'):
            
            
            segundoapellido[j]='X'
        
            continue



for i in range(len(segundoapellido)):
    
    
        if(segundoapellido[i] not in vocales and i>0):
            
            
            listacurp9.append(segundoapellido[i])
            
            break     

listacurp2=segundoapellido[0]


nombres=input("Ingresa tu nombre(s): ")
nombres=list(nombres)

for j in range(len(nombres)):
    
    
        if(nombres[j]=='Ñ'):
            
            
            nombres[j]='X'
        
            continue





for i in range(len(nombres)):
    
    
        if(nombres[i] not in vocales and i>0):
            
            
            listacurp9.append(nombres[i])
            
            break


listacurp3=nombres[0]


anacimiento=input("Ingresa tu año de nacimiento: ")
anacimiento.split()
listacurp4=anacimiento[2],anacimiento[3]
    

mes=input("Ingresa tu mes de nacimiento (01,02...): ")
listacurp5=mes


dia=input("Ingresa tu dia de nacimiento (01,02...): ")
listacurp6=dia

genero=input("Ingresa tu género (H) o (M): ")
listacurp7=genero

estadoin=input("Ingresa tu estado de nacimiento: ")

if(estadoin=='QUERETARO' or estadoin=='CAMPECHE'):

    for key, value in estados.items():
        if key == estadoin:
            estadoin = value
            listacurp8=value
            break
else:    


    estadoin.split()


    longitud=len(estadoin)
    numEspacios=0


    for i in range(longitud):
        
        
        if(estadoin[i] in espacioblanco):
            numEspacios=numEspacios+1
            
            
    for k in range(longitud):
           
        if(numEspacios==1):
            if(estadoin[k] in espacioblanco):
                listacurp8=estadoin[0], estadoin[k+1]
                break

        else:
            if(estadoin[k] in espacioblanco and k>5):
                listacurp8=estadoin[0], estadoin[k+1]
                break
            
            
            
           
    if(k>=longitud-1):   

        for j in range(longitud):
            
            
            if(estadoin[longitud-1] not in vocales):              
                listacurp8=estadoin[0], estadoin[longitud-1]
                break
            
                
            else:   
                longitud=longitud-1





string1 = "".join(str(x) for x in listacurp)
string2 = "".join(str(x) for x in listacurp2)
string3 = "".join(str(x) for x in listacurp3)
string4 = "".join(str(x) for x in listacurp4)
string5 = "".join(str(x) for x in listacurp8)
string6 = "".join(str(x) for x in listacurp9)


primeraparte=string1+string2+string3

if(primeraparte not in palabrasGroseras):
    curp=string1+string2+string3+string4+listacurp5+listacurp6+listacurp7+string5+string6
    print(curp)

else:
    
    primeraparte=list(primeraparte)
    for i in range(len(primeraparte)):
        
        
            if(primeraparte[i] in vocales and i>0):
                
                
                primeraparte[i]='X'
                string7 = "".join(str(x) for x in primeraparte)
                curp=string7+string4+listacurp5+listacurp6+listacurp7+string5+string6
                print(curp)
                break



