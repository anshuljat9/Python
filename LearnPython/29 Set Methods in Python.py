cities  = {'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'} 

cities2 = {'New York', 'Los Angeles', 'Houston', 'Phoenix', 'San Francisco'}

cities3 = {'New York', 'Los Angel', 'Phoenix'}

# # Adding a city to the set
# cities.add('San Francisco')
# # Removing a city from the set
# cities.remove('Chicago')  # Raises KeyError if 'Chicago' is not in the set

cities3 = cities.union (cities2)  # This will raise TypeError because sets cannot be concatenated

cities4 = cities.intersection(cities2)  # This will return the common elements between the two sets

cities5 = cities.symmetric_difference(cities2) # This will return the elements that are in either set but not in both

cities6 = cities.difference(cities2)  # This will return the elements that are in cities but not in cities2


print (cities3) 
print (cities4)
print (cities5)
print (cities6)

print (cities.isdisjoint(cities2))  # This will return True if the two sets have no elements in common

print (cities.issuperset(cities2))  # This will return True if cities contains all elements of cities2

print (cities.issubset(cities3))  # This will return True if cities is a subset of cities3

cities7 = cities.add('San Francisco')  # This will add 'San Francisco' to the set cities
print(cities7)  # This will print None because add() does not return anything
 
cities8 = cities.update({'berlin', 'paris'})  # This will add 'berlin' and 'paris' to the set cities
print(cities8)  # This will print None because update() does not return anything 

cities9 = cities.remove('Chicago')  # This will remove 'Chicago' from the set cities
print(cities9)  # This will print None because remove() does not return anything

cities10 = cities.discard('Houston')  # This will remove 'Houston' from the set cities if it exists
print(cities10)  # This will print None because discard() does not return anything

cities11 = cities.pop()  # This will remove and return an arbitrary element from the set cities
print(cities11)  # This will print the element that was removed

cities12 = cities.clear()  # This will remove all elements from the set cities
print(cities12)  # This will print None because clear() does not return anything

cities69 = {'Berlin', 'Paris', 'Madrid'}
del cities69  # This will delete the set cities
# This will raise NameError because cities is deleted
