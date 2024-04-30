#making a list of lines from a file

#since the object gotten in with after open is done is kept within the with block,
#we can create a list of lines that will be used outside the with block

with open('pi_digits.txt') as file_object:
    lines=file_object.readlines() #readlines takes each line in object and stores it
                                    #in a list. the list is then assigned to lines

for line in lines:
    print(line.rstrip())


#we can now start working with the file's content after it is loaded to the memory.

with open('pi_digits.txt') as file_object:
    lines=file_object.readlines()

#lets make an attempt to print the contents of the pi without any whitespaces

pi_string=''
for line in lines:
    pi_string+=line.rstrip()

print(pi_string)
print(len(pi_string))
print(len(pi_string[:10]))

pi_string=float(pi_string)

pi=pi_string+1
print(pi)

