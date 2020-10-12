print("Skriv inn koordinatene under")
x1 = int(input("X1: "))
y1 = int(input("Y1: "))
x2 = int(input("X2: "))
y2 = int(input("Y2: "))
print("Du har oppgitt koordinatene (", x1, ",", y1, "),(", x2, ",", y2, ")")
if (x2 - x1) == 0:
    print("Dette er en rett linje x=",x1,)
elif (y2-y1) == 0:
    print("Dette er en rett linje y=",y1,)
else:
    a = ((y2 - y1) / (x2 - x1))
    b = (y1 - a * x1)
    print ("Vi får da ligningen ",a,"x + ",b,sep="")