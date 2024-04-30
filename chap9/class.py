class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(f"{self.name} is now sitting")


my_dog=dog('willie',6)
print(f"my dog's name is {my_dog.name}.")

my_dog.sit()
dog.sit(my_dog)
#as you can see from above, there are two ways of calling methods in a class