##Pi zza Project for Code Louisville python may 2020

def select_time():
    TimeSlots = ['6:00 - 6:15', '6:15 - 6:30', '6:30 - 6:45', '6:45 - 7:00']    
    length = len(TimeSlots)
    i = 0 
    while i < length:
    displayCounter = i + 1
    print (str(displayCounter)+ "). " + TimeSlots[i])
    i +=1

##def order_pizza():


first_name = input('Hello what is your name?  ')
order_pizza = input("Hello {} would you like to order a pizza?   Y/N   ".format(first_name)).upper()


if order_pizza == 'Y':
   print("Awesome Sauce! Let's get started.")
    select_time()
    ##order_pizza() 
else:
    print("No worries! Have a great day.")


    




# while True:
#     try:
  
# except NameError:
#     print("Sorry, please type Y or N for your answer.")
#     continue
# else:
#     break
# if order_pizza == "Y":
    


    
