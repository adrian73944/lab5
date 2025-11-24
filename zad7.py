def potegi(a,n):
    if n==0:
        return 1
    else:
        return a*potegi(a,n-1)

a = int(input("Podaj liczbę: "))
n= int(input("Podaj potęgę:"))
print(potegi(a,n))