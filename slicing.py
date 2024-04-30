#applicable when one wants to work with part of a list and not the entire list.
players=['charles','martina','michael','florence','eli']
print(players[0:4])
#you can choose to omit the first number in the range. python will start from the beginning.
print(players[:3])
#similarly, if you want to print from a specified area to the last, you can omit the second input
print(players[2:])
#if you want to print the last two elements in a list
print(players[-2:])
#if a third item is included in the brackets, it tells python by how many times it should skip 
#between items.

#we can use a for loop through a slice.
print("here are the first three players to win the race\n")
for player in players[:3]:
    
    print(player.title())
    print("\n")
