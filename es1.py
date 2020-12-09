print("Scrivi una parola:   ")
parola=list(input())
palindromo=[]
for l in parola:
    palindromo.append(l)
palindromo.reverse()
print()
if parola==palindromo:
    print("Questa parola è un palindromo")
else:
    print("Questa parola non è un palindromo")