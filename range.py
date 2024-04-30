#the range() function is used to input numbers from the first number to the number before the 
#one specified in the paramater parenthesis.
for value in range(1,5):
    print (value)

#as for this funtion it will print the numbers from 1,2 3,4
#passing one argument in the range () will print the numbers from 0 to that number in the parenthesis.

#to convert the range() omtp a list one has to use the list() function and in its parenthesis purse range()
numbers=list(range(1,6))
print(numbers)
#note that if you pass a third number in the range() the range function will use it as a skip size for the numbers that will be printed.
even_numbers=list(range(2,11,2))
print(even_numbers)

#a program to find squrares of numbers ranging from 1 to 10
squares=[]
for value in range(1,11):
    square=value ** 2
    squares.append(square)

print(squares)