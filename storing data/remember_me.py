import json
filename = 'whotoremember.json'
try:
    with open(filename) as f:
        username = json.load(f)

except FileNotFoundError:
    username = input("please enter your username ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"be sure we'll remember you when you come back, {username}")

else:
    print(f"hello {username}")
