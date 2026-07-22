s = {2,6,9,3,5,7,8,1,4}
print(s)

# Sets are unordered collections of unique elements 
# They are mutable, meaning you can add or remove elements 
# They do not support indexing, slicing, or other sequence-like behavior
# Sets are defined using curly braces or the set() constructor

# Example of creating a set
s1 = {1, 2, 3, 4, 5}

s2 = set([1, 2, 3, 4, 5])

# Example of creating an empty set
s3 = set()
print(type(s3))  # <class 'set'>

# Example of creating a set with mixed data types
s4 = {1, "hello", 3.14, (1, 2)}

# Example of creating a set with duplicate elements
s5 = {1, 2, 2, 3, 4}  # Duplicates are removed

# Example of creating a set with a range of numbers
s6 = set(range(1, 11))  # Creates a set with numbers from 1 to 10

# Example of creating a set from a string
s7 = set("hello")  # Creates a set with unique characters from the string

# Example of creating a set from a list
s8 = set([1, 2, 3, 4, 5])  # Creates a set from a list

# Example of creating a set from a tuple
s9 = set((1, 2, 3, 4, 5))  # Creates a set from a tuple

# Example of creating a set from a dictionary (keys only)
s10 = set({"a": 1, "b": 2, "c": 3})  # Creates a set from dictionary keys   

# Example of creating a set from a frozen set
s11 = set(frozenset([1, 2, 3, 4, 5]))  # Creates a set from a frozenset

# Example of creating a set with a comprehension
s12 = {x for x in range(1, 11) if x % 2 == 0}  # Creates a set of even numbers from 1 to 10

# Example of creating a set with a generator expression
s13 = set(x for x in range(1, 11) if x % 2 == 0)  # Creates a set of even numbers from 1 to 10

# Example of creating a set with a nested comprehension
s14 = {x for x in range(1, 11) if x % 2 == 0 for y in range(1, 4)}  # Creates a set of even numbers from 1 to 10 with nested comprehension

# Example of creating a set with a nested generator expression
s15 = set(x for x in range(1, 11) if x % 2 == 0 for y in range(1, 4))  # Creates a set of even numbers from 1 to 10 with nested generator expression


print (s1)
print (s2)
print (s3)
print (s4)
print (s5)
print (s6)
print (s7)
print (s8)
print (s9)
print (s10)
print (s11)
print (s12)
print (s13)
print (s14)
print (s15)

