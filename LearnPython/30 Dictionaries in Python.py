info = {'name': 'John', 'age': 30, 'city': 'New York'}
print(info)
# Accessing values
print(info['name'])  # Output: John
print(info.get('name'))  # Output: John 

print(info.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(info.values())  # Output: dict_keys(['name', 'age', 'city'])

for key in info:   
    print(f"The Value of the corresponding to the key {key} is {key, info[key]}")

print (info.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

for key , value in info.items():   
    print(f"The Value of the corresponding to the key {key} is {value}") 