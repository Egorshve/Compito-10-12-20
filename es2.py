numeroparole=int(input("Quante parole vuoi inserire?   "))
contatore=0
listaparole=[]
listanumeri=[]
while contatore!=numeroparole:
    parola=input("Inserisci la parola:   ")
    listaparole.append(parola)
    listanumeri.append(len(parola))
    contatore+=1
print()
print(listaparole)
print(listanumeri)