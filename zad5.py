def funkcja(waga,wzrost):
    bmi= waga/(wzrost**2)
    if bmi<18.5:
        print("niedowaga")
    elif bmi>=18.5 and bmi<25:
        print("dobra masa ciała")
    elif bmi>=25 and bmi<30:
        print("nadwaga")
    elif bmi>=30 and bmi<35:
        print("otyłość 1 stopnia")
    elif bmi>=35 and bmi<40:
        print("otyłość 2 stopnia")
    elif bmi>=40:
        print("otyłość 3 stopnia")

waga=float(input("podaj waga:"))
wzrost=float(input("podaj wzrost:"))
funkcja(waga,wzrost)
