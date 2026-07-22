'''Phyton List'''

lst = [3,5,6,88]
print(type(lst))
print(lst)

'''List Index'''

color = ["Red","Yellow","Green","White","Purple","Blue"]
        # [0]     [1]     [2]     [3]     [4]      [5]

print(color[3])

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
       # [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])

# if "no" in colors:
#     print("yes")

# else:
#     print("no")

'''Range Of Index'''

# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[2:7])	#using positive indexes
# print(animals[-7:-2])	#using negative indexes'

'''Jumping'''
# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[1:8:3])

'''List Comprehension'''
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)


