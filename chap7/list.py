
members={}
active=True
while active:
    name=input("enter the name of the member: ")
    if name=='n':
        active=False
    attributes=[]
    more=True
    while more:
        attribute=input("enter the attributes of the member")
        attributes.append(attribute)
        if attribute=='n':
            members[name]=attributes
            more=False
    

print(members)