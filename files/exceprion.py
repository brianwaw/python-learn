num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ")

#convert input string into integers if integers are entered
if num_1.isdigit() and num_2.isdigit():
    num_2 = int(num_2)
    num_1 = int(num_1)

else:
    print("Enter valid numbers")

try:
    answer = num_1 / num_2

except ZeroDivisionError:
    print("You cannot divide a number to zero")

#code that depends on try code to be fully executed first
else:
    print(answer)

#an attempt to handle file not found exception

path = 'brian.txt'

try:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()


except FileNotFoundError:
    print(f"{path} is not found.")

