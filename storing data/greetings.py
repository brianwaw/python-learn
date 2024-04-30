#a program to prompt a user to enter their name and later on greet them

import json
username = input("please enter your username")
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)

with open(filename) as j:
    user = json.load(j)

print(f"we did not forget you {user}")


