# in a list, we check if it's empty when we use a colon after the name of the list in if statement.
# it returns true if there are values in the list and false if there are no values in the list.
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"adding {requested_topping.title()}")
else:
    print("are you sure you don't want a topping for your pizza?")
