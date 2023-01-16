text='ggdfurrosdsdfsfdfsdgfdsfsdfsdfsdffurrosodkfdvknfkvdf'
palabra='furros'
palabra=list(palabra)
long=len(text)
longpalabra=len(palabra)
text=list(text)
word=[]
x=0

for i in range(longpalabra):
    for j in range(long):
        if(text[j]==palabra[x]):
            word.append(text[j])
            x=x+1
            
            if(x>1):
                for k in range(len(word)):
                    if(word[k]==text[j-1] and word[k+1]==text[j]):
                        print(word[0],word[1])
                        break
            
