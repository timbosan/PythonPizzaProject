##Pizza Project for Code Louisville python may 2020

def select_time():
    TimeSlots = ['6:00 - 6:15', '6:15 - 6:30', '6:30 - 6:45', '6:45 - 7:00']    
    i = 0
    displayCounter = i + 1
    print('\nPlease Select a pick-up time slot, by selecting the number by the time slot you choose.')
    for times in range(len(TimeSlots)):
        print ('\n'+str(displayCounter)+ "). " + TimeSlots[i] + '\n')
        displayCounter +=1
    UserTimeSelect = input()
    UserTimeChoice = int(UserTimeSelect) -1 
    print("Great you've Selected {}, as your pick up window!\n".format(TimeSlots[UserTimeChoice]))


def order_pizza():
    print("What do you want on the pizza?")


first_name = input('Hello what is your name?  ')
order_pizza = input("Hello {} would you like to order a pizza?   Y/N   ".format(first_name)).upper()


if order_pizza == 'Y':
    print("Awesome Sauce! Let's get started.")
    select_time()
    order_pizza() 
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
    
  # length = len(TimeSlots)
    # i = 0 
    # while i < length:
    # displayCounter = i + 1
    # print (str(displayCounter)+ "). " + TimeSlots[i])
    # i +=1

    
