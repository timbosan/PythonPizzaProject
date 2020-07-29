##Pizza Project for Code Louisville python may 2020
import datetime

def days_til_friday():
    today = datetime.date.today()
    friday = today + datetime.timedelta( (4-today.weekday()) % 7 )
    til_friday = (friday - today)
    return til_friday.days

##Function to select Pizza pickup time.
def select_time():
    time_slots = ['6:00PM - 6:15PM', '6:15PM - 6:30PM', '6:30PM - 6:45PM', '6:45PM - 7:00PM']    
    i = 0
    print('Please Select a Friday pick-up time, by selecting the number by the time slot you choose.')
    for i, time in enumerate(time_slots):
        print(f'{str(i+1)}. {time}')
    user_time_select = input()
    user_time_choice = int(user_time_select) -1 
    print("\nGreat you've Selected {}, as your pick up window!".format(time_slots[user_time_choice]))
    return(time_slots[user_time_choice])
    

##Function to select toppings for pizza
def order_pizza():
    topping_choices = ['Pepperoni', 'Italian Sausage', 'Jalapeno', 'Mushroom', 'Hot Honey','Basil']
    customer_topping_choices = []
    i = 0 
    print("What do you want on the pizza?")
    for i, toppings in enumerate (topping_choices):
        print(f'{str(i+1)}. {toppings}')
    print('0. Done')
    user_topping_select = ''
    while user_topping_select != '0':
        user_topping_select = input('Select a topping: ')
        if user_topping_select != '0':
            user_topping_choice = int(user_topping_select) -1
            customer_topping_choices.append(topping_choices[user_topping_choice])
            print("These are you toppings so far: {}".format(', '.join(customer_topping_choices)))
    return customer_topping_choices

##Function that gives you overview of order and toppings
def order_result():
    print(f'\nYou ordered a {", ".join(order_topping_choice)} pizza. Please pick it up between {order_time_choice}.\n')

##Main code
first_name = input('\n\nHello what is your name?  ') 
ask_to_order = input("\n\nHello {} would you like to order a pizza?   Y/N   ".format(first_name)).upper()


if ask_to_order == 'Y':
    print("\n\nAwesome Sauce! Let's get started.")
    order_time_choice = select_time()
    
    while (True):
        order_topping_choice = order_pizza() 
        print(f'Great you have ordered a pizza with {", ".join(order_topping_choice)} on it.')
        another_pizza = input('Would you like to order another pizza?   Y/N  ').upper()
        if another_pizza == 'N':
           break
    order_result()
    til_friday = days_til_friday()
    print (f'See you in {til_friday} days!!')
   
else:
    print("\n\nNo worries! Have a great day.")








    
