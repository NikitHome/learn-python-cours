requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping:
    print("Adding mushrooms!")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni!")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese!")
    
print("\n")



requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinishing, making your pizza!")
else: 
    print("Are you sure you want a plain pizza?")
    
    

avialable_toppings = ['mushrooms', 'olives', 'extra cheese', 'green papers', 
                      'pipperoni', 'pineapple']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in avialable_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
        
print("\nFinished making your pizza!")