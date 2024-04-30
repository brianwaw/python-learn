user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
for key, value in user_0.items():
    print(f"key:{key}")
    print(f"value:{value}\n")
    
favorite_language={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name,language in favorite_language.items():
    print(f"name:{name}")
    print(f"language:{language}\n")

#the method .items() is used when one wants to acquire both key and value. if one wants key only
#use the normal format of for loop. you can also use the .keys() method instead of .items()
for name in favorite_language:
    print(f"name:{name}")

if 'waweru' not in favorite_language.keys():
    print("nigga state your favorite language")

#if you want to loop through a dictionary's keys in a particular order, use the sorted method
for name in sorted(favorite_language.keys()):
    print(f"{name.title()}, thank you for takint the poll.")

#to get values in a loop of dictionaries, use the values() method.
print("these are the languages that got chosen in the poll")
for languages in favorite_language.values():
    print(f"\n{languages}")

#to ensure that there is no repetition, use the set() around the dictionary that contains the duplicate
for languages in set(favorite_language.values()):
    print(f"\n{languages}")

#to loop through a dictionary's keys in a particular order, first you have to use the sorted() 
#method
for name in sorted(favorite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll")


