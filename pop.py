motorcycles=['honda','yamaha','suzuki']
#assuming that the motorcycles are inputed according to the one that came last, we use pop to
#determine the motorcycle that came last
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
#if you want to pop an item from the list that is at any point, use the pop(index)
bicycles=['bmx','phillips','jeep']
#assuming that the bicycles are keyed as they enter the store, we can get the first bicycle to 
#arrive by:
first_bike=bicycles.pop(0)
print(first_bike)

