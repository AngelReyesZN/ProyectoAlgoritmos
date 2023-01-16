lista=[5,3,2,4,1,8,9,7]
lista1=[]
lista2=[]
lista3=[]


def partir_lista(lista):
    
    separarlista=len(lista)/3
    separarlista=int(separarlista)
    lista1=lista[:separarlista]
    lista2=
    lista3=lista[separarlista:]
    return lista1,lista2,lista3


def ordenamiento(lista):
    for i in range(len(lista)):
        minimo=min(lista[i:])
        indiceminimo=lista.index(minimo)
        indiceacambiar=i
        lista[indiceminimo],lista[indiceacambiar]=lista[indiceacambiar],lista[indiceminimo]
    return lista



lista1, lista2, lista3=partir_lista(lista)


lista1=ordenamiento(lista1)

lista2=ordenamiento(lista2)

lista3=ordenamiento(lista3)

listafinal=lista1+lista2+lista3

listafinal=ordenamiento(listafinal)




