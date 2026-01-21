print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, L: \n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n")
extra_cheese = input("Do you want extra cheese? Y or N: \n")
pizza_price = 0

#if we choose pepperoni $3 will be added
#if we choose extra cheese $10 will be added
if (size == "S"):
    pizza_price = 15
elif (size == "M"):
    pizza_price = 20
elif (size == "L"):
    pizza_price = 25

if (pepperoni == "Y"):
    pizza_price += 3
elif (pepperoni == "N"):
    pizza_price += 0

if (extra_cheese == "Y"):
    pizza_price += 5
elif (extra_cheese == "N"):
    pizza_price += 0

print(pizza_price)