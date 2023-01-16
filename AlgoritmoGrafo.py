matriz=[[99,7,9,8],
        [7,99,12,12],
        [9,12,99,10],
        [8,12,10,99]
        ]

for i in range(4):
    minimorenglon=min(matriz[i])
    indicei=[i]
    indicej=matriz[i].index(minimorenglon)
    
    for j in range(4):
        print(matriz[i][j])
        
    