figura=0
while figura!=5:
    print()
    print()
    print("Di quale figura vuoi calcolare l'area tra....(inserire numero)")
    print("1.Quadrato")
    print("2.Rettangolo")
    print("3.Triangolo")
    print("4.Cerchio")
    print("Oppure premi 5 per terminare")
    figura=int(input())
    print()
    if figura==1:
        print("Figura: QUADRATO")
        print()
        lato=float(input("Quanto misura il lato in cm?"))
        area=lato*lato
        print()
        print("L'area del quadrato è",area,"cm2")
    if figura==2:
        print("Figura: RETTANGOLO")
        print()
        base=float(input("Quanto misura la base in cm?"))
        altezza=float(input("Quanto misura l'altezza in cm?"))
        print()
        area=base*altezza
        print("L'area del rettangolo è",area,"cm2")
    if figura==3:
        print("Figura: TRIANGOLO")
        print()
        base=float(input("Quanto misura la base in cm?"))
        altezza=float(input("Quanto misura l'altezza in cm?"))
        print()
        area=base*altezza
        area=area/2
        print()
        print("L'area del triangolo è",area,"cm2")
    if figura==4:
        print("Figura: CERCHIO")
        print()
        raggio=float(input("Quanto misura il raggio in cm?"))
        print()
        area=raggio*raggio*3.14
        print("L'area del cerchio è",area,"cm2")
