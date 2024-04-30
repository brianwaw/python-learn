
with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents)

with open('pi_digits.txt') as f:
    contents = f.read()

print (contents.rstrip())

#use the above to access contents of a file . in this example the path of the 
#text file is not needed since it is in the same folder as the program needing it