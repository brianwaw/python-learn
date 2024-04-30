filename='programming.txt'
#an extra argument has to be passed in the open function telling it that you want
#to write to the file.

with open(filename,'w') as file_object:
    file_object.write("i love programming as hell\n")
    file_object.write("i love creating new games\n")


# 'w' tells pythan that we want to open the file in write mode
#'r' read mode, 'a' append mode or a mode to allow reading and writing to the file 'r+'
# if you open the file without the second argument it will be read only by default.

#we write to the object using the write() method where we pass in the data in it

#python can only write strings to text files hence to store numerical data in text files
#you have to convert the data to string format first using the str() function.

#remember to include new lines since write() doesn't do so after writing line.

