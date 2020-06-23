##Pi zza Project for Code Louisville python may 2020

first_name = input('Hello what is your name?  ')
order_pizza = input("Hello {} would you like to order a pizza?   Y/N   ".format(first_name)).upper()

if order_pizza == "Y":
    print("Awesome Sauce! What time slot on Friday works best for you?")
else:
    print("No worries! Have a great day.")