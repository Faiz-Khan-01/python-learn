'''
simple income tax calculator.(Nirmala simulator)
This program calculates your income tax percentage based on your income.

'''
print("Welcome, \nThis is an income tax calculator.\nPlease enter number only, otherwise the program won't work.")
a=float(input("\nPlease Write your monthly income (which is in ₹) below.\n"))
if int(a) < 34001 :
    print("\nYour income is too low to be taxed.")
elif int(a) < 67001 : 
    print("\nThere would be just 5% tax on your income which would be", a/5 ,"₹" )
elif int(a) < 100001 :
    print("\nThere would be just 10% tax on your income which would be", a/10 ,"₹" )
elif int(a) < 134001 :
    print("\nThere would be 15% tax on your income which would be", a/15 ,"₹")
elif int(a) < 165001 :
    print("\nThere would be 20% tax on your income which would be", a/20 ,"₹")
elif int(a) < 200001 :
    print("\nThere would be 25% tax on your income which would be", a/25 ,"₹" )
elif int(a) < 300001 :
    print("\nThere would be 30% tax on your income which would be", a/30 ,"₹\nBTW you're so rich.")
else :
    print("\nThere would be 35% tax on your income which would be", a/35 ,"₹\nBTW DAMN!! You're SO rich.")

# I hope you liked my project.