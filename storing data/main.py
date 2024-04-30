#we use json.dump() and json.load() to store and retrieve the user inputed data.
#first thing is to store the data. we use the json.dump() to store
#json.dump() takes two arguments: a piece of data to store and a file object it can use
#to store the data.

import json
numbers = [1, 2, 3, 4, 5]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
