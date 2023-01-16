lista=["ANGEL REYES"] #ESTADO CON UN ESPACIO
listados=['BAJA CALIFORNIA SUR']
listadd=[]
espacioblanco=[' ']
espacioblanco2=[' '' ']
separado=[]
letraterminacion=['S','Z','N','T']
vocales=['A','E','I','O','U']

estado = None	
estados = { 
    '':'', 'CAMPECHE':'CC', 'QUERETARO':'QT',
		}


# estadoN=input("Introduce tu estado: ")
# estado = None	
# estados = { 
#     '':'', 'CAMPECHE':'CC', 'QUERETARO':'QT', 'SAN LUIS POTOSI':'SP',
# 		}
# 
# for key, value in estados.items():
#     if key == estadoN:
#         estadoN = value
#         break
# 



listass=list(lista[0])

# string = "".join(str(x) for x in listass)
# print(string)
# 
# listadd.append(string)


for i in range(len(listass)):
    maximo=max(listass[i:])
    
    
    
penultimo= len(listass)-2

print(listass[penultimo])


separado2=input("Introduce tu estado: ")

if(separado2=='QUERETARO' or separado2=='CAMPECHE'):

    for key, value in estados.items():
        if key == separado2:
            separado2 = value
            print(value)
            break
else:    


    separado2.split()


    longitud=len(separado2)
    numEspacios=0


    for i in range(longitud):
        
        
        if(separado2[i] in espacioblanco):
            numEspacios=numEspacios+1
            
            
    for k in range(longitud):
           
        if(numEspacios==1):
            if(separado2[k] in espacioblanco):
                print(separado2[0], separado2[k+1])
                break

        else:
            if(separado2[k] in espacioblanco and k>5):
                print(separado2[0], separado2[k+1])
                break
            
            
            
           
    if(k>=longitud-1):   

        for j in range(longitud):
            
            
            if(separado2[longitud-1] not in vocales):              
                print(separado2[0], separado2[longitud-1])
                break
            
                
            else:   
                longitud=longitud-1
    
             
            
            
            
            
            
#             continue
#         
#         
#         else:
#     #         continue 
#     #         longitud=longitud-1
# 
#             if(separado[longitud-1] not in vocales):
#                 
#                 print(separado[0], separado[longitud-1])
#                 break
                        
        
        
#     if(separado[i] in espacioblanco2 and i>5):
#         print(separado[0], separado[i+1]) 
        
        
        
        
# for i in range(len(lista)):

#     
#     if(separado[i] in espacioblanco):
#         print(separado[0], separado[i+1])
#         break       
#         
        
        

        
        
