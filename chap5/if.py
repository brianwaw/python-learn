#this is used in conditional tests.
#suppose we have written cars in they respective names but want to write bmw in upper case
#and the other cars in title case, we can do the following

cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#there are several if scenarios. one is the standard if statement which only allows one condition 
#another one is the if - else statement which is the best when one wants to evaluate a scenario and 
#give a different feedback when the given conditions are either true or false. it works with two 
#possible situations.

#when one wants to work with more than two situations, you should work with the if-elif-else chain.
#for instance a code for different charges for entrance in an amusement partk
#note that in the if-elif-else condition, after finding the condition that passes, the program 
#gets out of the if statement.

#if at all you want to evvaluate more than one scenario, you ought to use the many if statements.

requested_topping=['mushrooms','extra cheese']

if 'mushrooms' in requested_topping:
    print("adding mushrooms")
if 'pepperoni' in requested_topping:
    print("adding pepperoni")
if 'extra cheese' in requested_topping:
    print("adding extra cheese")












age=12
if age<4:
    print("pay zero shillings")
elif age <18:
    print("pay 200 shillings as your entrance fee")
else:
    print("pay 1000 as your entrance fee")

#python does not require an else statement in the end of an if elif else statement. it is better 
#to sometimes use another elif to capture a specific condition.
#the else is a catchall condition that includes even malicious or even typos.