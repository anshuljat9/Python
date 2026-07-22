'''Converting tuple to string'''

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("china")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

'''Tuple count method'''
tuple = (1,2,3,4,5,6,7,8,9,0,3,3,3,3,3)
cou = tuple.count(3)
cou = tuple.index(3)
print("counting of 3 in tuple is :",cou) 