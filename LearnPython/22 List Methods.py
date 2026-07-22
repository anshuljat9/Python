'''Sort()'''

color = ["voilet", "indigo", "blue", "green"]
color.sort(reverse=True)
print(color)


'''Reverse()'''
color = ["voilet", "indigo", "blue", "green"]
color.reverse()
print(color)

'''Index()'''
color = ["voilet", "indigo", "blue", "green"]
colors = color.index("green")
print(colors)

'''Count()'''
color = ["voilet", "indigo", "blue", "green","red"]
colors = color.count("red")
print(colors)

'''Copy()'''
colors = ["voilet", "green", "indigo", "blue"]
new_list = colors.copy()
print(colors)
print(new_list)

'''append() This method appends items to the end of the existing list'''
colors = ["voilet", "green", "indigo", "blue"]
colors.append("red")
print(colors)

'''insert()'''
colors = ["voilet", "indigo", "blue"]
colors.insert(1 , "red")
print(colors)

'''extends'''
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)

'''Concatenating two list'''
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)