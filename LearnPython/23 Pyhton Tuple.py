'''If we put to many number or strings in () this type is tuple '''
tup = (2 ,4,34,46,56,7, 434)
print(type(tup), tup)

''' If we only put one number then it represent as 'int'''
tup = (2)
print(type(tup), tup)

'''Tuple Indexes'''
country = ("China", "Japan" , "Thailand")
print(type(country), country)

'''Positive Indexing & Negative Indexing'''
country = ("China", "Japan" , "Thailand")
#            [0]      [1]        [2]

print(country[0])
print(country[1])
print(country[2])

print(country[-1])
print(country[-2])
print(country[-3])
'''checking if item is presenting or not'''
if "China" in country:
    print("yes")
else:
    print("No")

'''Range in index'''
print(country[0:3:2])