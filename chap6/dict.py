#dictionaries are important in the sense that they enable us to store information about a partcular
#entity
#a dictionary is a collection of key-value pairs. each key is connected to a value, and you can
#use the key to access the value associated with the key.
#dictonaries are wrapped in curly braces{}
alien_0={'color':'green','points':5}
#to access a value in a dictionary, give the name of the dictionary and then place the key inside
#a set of square brackets

print(alien_0['color'])
#to add new key value pairs, state the name of the dictionary and then open the square braces
#enter the key and later on equate it to the value of your choice.
alien_0['y_position']=0
alien_0['x_position']=25
print(alien_0)
#it's actually convenient to start with an empty dictionary and then filling it's components one by one
alien_1={}
alien_1['color']='yellow'
alien_1['points']=5
#to modify the values in a dictionary, 
alien_1['color']='red'
print(alien_1)