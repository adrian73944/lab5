def powitanie(imie="Użytowniku", jezyk="polski"):
    if jezyk == "polski":
        print("Cześć "+imie)
    elif jezyk == "angielski":
        print("Hello "+imie)
    elif jezyk == "niemiecki":
        print("Guten Morgen "+imie)
    else:
        print("Witaj "+imie)

#Imie=str(input("podaj imie:"))
Jezyk=str(input("podaj jezyk:"))

powitanie()


