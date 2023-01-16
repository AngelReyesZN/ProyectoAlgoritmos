listadinero=[100,50,20,10,5,2,1]
cambiopordar=81
monedasfinal=0

#necesitamos saber la denominacion
for i in range(len(listadinero)):
    unidadesmonetarias=cambiopordar/listadinero[i]
    unidadesmonetarias=int(unidadesmonetarias)
    if(unidadesmonetarias>=1):
        cambiopordar=cambiopordar-unidadesmonetarias*listadinero[i]
        monedasfinal=monedasfinal+unidadesmonetarias
        print("Se pueden dar ", unidadesmonetarias,"monedas que valen: " , listadinero[i])
    else:
        x=0
        
        
print("Se necesita un total de: " , monedasfinal," monedas para dar cambio")
