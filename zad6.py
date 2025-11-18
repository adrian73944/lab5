def pole(a,b,c):
    if a<=0 or b<=0 or c<=0:
        print("nie mozliwe ze bok ma 0 lub mniej cm")
    elif a+b<=c or a+c<=b or b+c<=a:
        print("nie mozliwe")
    else:
    s=(a+b+c)/2
    pole=(s*(s-a)*(s-b)*(s-c))**(1/2)
    return pole

print(pole(1,2,3))