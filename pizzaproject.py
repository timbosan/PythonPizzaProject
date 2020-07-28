##Pizza Project for Code Louisville python may 2020


##Function to select Pizza pickup time.
def select_time():
    time_slots = ['6:00 - 6:15', '6:15 - 6:30', '6:30 - 6:45', '6:45 - 7:00']    
    i = 0
    print('\nPlease Select a pick-up time slot, by selecting the number by the time slot you choose.')
    for i, time in enumerate(time_slots):
        print(f'\n{str(i+1)}. {time}\n')
    user_time_select = input()
    user_time_choice = int(user_time_select) -1 
    print("\nGreat you've Selected {}, as your pick up window!".format(time_slots[user_time_choice]))
    return(time_slots[user_time_choice])
    

##Function to select toppings for pizza
def order_pizza():
    topping_choices = ['Pepperoni', 'Italian Sausage', 'Jalapenos', 'Mushrooms', 'Hot Honey','Basil', 'Finished Adding']
    i = 0 
    print("\nWhat do you want on the pizza?\n")
    while (user_topping_select != 8)
    
    for i, toppings in enumerate (topping_choices):
        print(f'\n{str(i+1)}. {toppings}\n')
    user_topping_select = input()
    user_topping_choice = int(user_topping_select) -1
    print("\nGreat you've selected to top your pizza with {}!".format(topping_choices[user_topping_choice]))
    return(topping_choices[user_topping_choice])

##Function that give you overview of order and toppings
def order_result():
    print(f'\nYou ordered a {order_topping_choice} pizza. Please pick it up between {order_time_choice}.\n')

##Main code
first_name = input('\n\nHello what is your name?  ') 
ask_to_order = input("\n\nHello {} would you like to order a pizza?   Y/N   ".format(first_name)).upper()


if ask_to_order == 'Y':
    print("\n\nAwesome Sauce! Let's get started.")
    order_time_choice = select_time()
    order_topping_choice = order_pizza() 
    order_result()
else:
    print("\n\nNo worries! Have a great day.")


    




# while True:
#     try:
  
# except NameError:
#     print("Sorry, please type Y or N for your answer.")
#     continue
# else:
#     break
# if order_pizza == "Y":
    
  # length = len(TimeSlots)
    # i = 0 
    # while i < length:
    # displayCounter = i + 1
    # print (str(displayCounter)+ "). " + TimeSlots[i])
    # i +=1

    
