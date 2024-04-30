#use modules to store functions so that they can be reused in many files.
#pizza.py is the name of my module and it will hold the function for the toppings
#to import a module, use the import
#to use the function use the syntax ## pizza.make_pizza(12,'pepperoni') 


#to import a specific function from a module, use the syntax
#from module_name import function_name
#for our case from pizza import make_pizza
#to use the function in this case use the name of the function without the dot operator


#sometimes the name of the function you are about to import might conflict with a name of an object
#in your code. to deal with that, use aliasing while importing the specific function
#note that the name of the imported function now changes 
#from pizza import make_pizza as mp
#now you will use mp()
#mp(12,'pepperoni')


#you can also alias a module
#import pizza as p
#p.make_pizza(12'pepperoni')


#you can also import all functions from a module into the file your program is at.
#this is the syntax from pizza import *
#now you will not need the dot operator
#make_pizza(12,'pepperoni')

