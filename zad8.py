#a)
def funkcja(*args):
   for arg in args:
        print(arg)

funkcja(1,"tekst", 10,"inf")
#b)
def funkcja1(*args):
    max=args[0]
    for arg in args:
        if arg>max:
            max=arg
    return max

print(funkcja1(1,4,10,2,4,6,11,40,))
