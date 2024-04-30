def greetings(users):
    for user in users:
        print(f"Hello {user.title()}, it's been a while")

users=['brian','allan','alex','sharon']
greetings(users)

#to prevent modification of the elements in a list while passing it to a function, use the copy
#of the list. use the knowledge on slicing for this. printmodels(unprinted[:])

#sometimes one could pass many arguments 
#use def make_pizza(*toppings). the asterisk makes an empty tupple named toppings hence
#many arguments can be passed as the user calls the function make_pizza
#ensure that the arbitrary parameters are keyed last. so as not to outdo calling.

def build_profile(first,last,**user_info):
    user_info['first_name']=first
    user_info['last_name']=last

    return user_info

user_profile=build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)