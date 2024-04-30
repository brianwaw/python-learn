#int() is applicable if you want to enter numbers and use them as numbers
#it converst the string into numerical value

age=input("how old are you ")
age=int(age)
if age>18:
    print("adult")

else:
    print("minor")
