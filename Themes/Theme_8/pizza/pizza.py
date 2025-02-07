def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(*toppings):
    print(f"\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        
make_pizza(16, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')