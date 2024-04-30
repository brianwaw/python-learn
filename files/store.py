#load the username, if the username file has been created previously.
#otherwise, prompt for the username and store it

import json
filename = 'username.json'

try:
    with open(filename) as f:
        username = json.load(f)

except FileNotFoundError:
    username = input("enter username")
    with open(filename, 'w') as f:
        json.dump(username, f)

else:
    print(f"welcome back {username}")



