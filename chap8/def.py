def greet_user():
    """"Display a simple greeting"""
    print("hello!")

greet_user()    
#the second line is a comment called a docstring which describes  what the function does
#python looks for the docstrings when generating documentation for the funtions in progr.

#parameters of the function are inserted in the braces after function name
#arguments for the same are passed during the function call
#positional arguments are the ones that follow the order in which the fuctions were entered
#keyword arguments don't need the order but instead the values are equated

def describe_pet_(pet_name,animal_type='dog'):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet_('willie','hamster')
