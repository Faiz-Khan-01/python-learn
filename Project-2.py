#This is a basic vote eligiblity program.
a=str(input("What is your name?  "))
b=int(input("What is your age?   "))
if(b) > 17 :
    print("\n\nCongrats",a, ",\nYou are elgible for voting.")
elif(b) < 17 :
    print("\n\nSorry", a,",\nYou aren't eligible for voting.")