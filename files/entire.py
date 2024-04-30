from pathlib import Path
path=Path('pi_digits.txt')
contents=path.read_text()
print(contents)

with open('pi_digits.txt') as file_object:
    contents=file_object.read()

print(contents.rstrip())

#use the above to access contents of a file . in this example the path of the 
#text file is not needed since it is in the same folder as the program needing it