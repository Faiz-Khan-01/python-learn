# This is a basic nutrition tracker program.
a=str(input("answer in yes or no only.\n\nDo you eat non-veg?\n"))
if (a=="yes") :
    print("you get enough protein.")
elif (a=="no") :
    print("you dont get enough protein.")
b=str(input("\nDo you eat grains?\n"))
if (b=="yes") :
    print("you get carbohydrates.")
elif(b=="no") :
    print("you dont get enough carbohydrates.")
c=str(input("\nDo you eat veggies and fruits?\n"))
if(c=="yes") :
    print("you get other many  nutrients.")
elif(c=="no") :
    print("You dont get other many nutrients.")

if (a=="yes") and (b=="yes") and (c=="yes") :
    print("\n\nGood job. You get all Nutrients.")
elif (a=="yes") and (b=="yes") or(c=="no") :
    print("\n\nYou dont get all other nutrients except protein and carbs.")
elif (a=="no") and (b=="yes") and (c=="yes") :
    print("\n\nYou get all nutrients except protein.")
elif (a=="yes") and (c=="yes") or (b=="no") :
    print("\n\nYou get all nutrients except carbohydrates.")
