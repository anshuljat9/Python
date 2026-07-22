'''# Upper()'''
str1 = "abcdefghijklmnopqrstuvwxyz"
print(str1.upper())

'''# # Lower()'''
str2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(str2.lower())

'''# # Strip() : The strip() method removes any white spaces before and after the string.'''

str3 = " Golden Day "
print(str3.strip())
print(str3)

''' # rstrip() : The rstrip() method removes any trailing characters (characters at the end of a string).'''
str4 = "hello ji !!!!!!!!!!!!!!!!!!!!!!!!!!"
print(str4.rstrip("!"))

'''# Replace() : The replace() method replaces a string with another string.'''
str5 = "My name is Jhon Chena"
print(str5.replace("Jhon", "Anshul"))

'''# split() : The split() method splits a string into a list.'''
str6 = "hey, nice to meet you, tom"
print(str6.split(" "))

'''#capitalize() : The capitalize() method returns a string where the first character is upper case.'''
str7 = "hello world!"
print(str7.capitalize())

'''# Center() : The center() method returns a centered string.'''
str8 = "Welcome to the Console!!!"
print(str8.center(50))

'''# count() : The count() method returns the number of times a specified value occurs in a string.'''
str9 = "hello world!"
print(str9.count("1"))

'''# endwith() : The endswith() method returns true if the string ends with the specified value.'''
str10 = "Welcome to the Console !!!"
print(str10.endswith("!!!"))
str10 = "Welcome to the Console !!!"
print(str10.endswith("to", 4, 10)) # 4 sai 10 tak dekhega

'''# find() : The find() method finds the first occurrence of the specified value.'''
str11 = "hello world!"
print(str11.find("l"))

'''# Index() : The index() method finds the first occurrence of the specified value.If given value is absent from the string then raise an exception.'''

'''# true condition'''
str12 = "He's name is Dan. Dan is an honest man."
print(str12.index("Dan"))

'''# false condition'''
# str12 = "He's name is Dan. Dan is an honest man."
# print(str12.index("Daniel"))

'''# isalnum() : The isalnum() method returns True if all the characters are alphanumeric (a-z, A-Z, 0-9).'''
str13 = "hello123"
print(str13.isalnum())

'''# isalpha() : The isalpha() method returns True if all the characters are in the alphabet (a-z, A-Z) is true, (0-9) is false.
str14 = "Hello1"
print(str14.isalpha())
"""

'''# islower() : The islower() method returns True if all the characters are in lower case.'''
str16 = "H!"
print(str16.islower()) 
print(str16.isupper())

'''# isprintable() : The isprintable() method returns True if all the characters are printable.'''
str17 = "hello world!"
print(str17.isprintable())

'''# isspace() : The isspace() method returns True if all the characters in a string are whitespaces.'''
str18 = "  "
print(str18.isspace())

'''# istitle() : The istitle() method returns True if the string follows the rules of a title.'''
str19 = "World Health Organization" 
print(str19.istitle())

'''# startswith() : The startswith() method returns True if the string starts with the specified value.'''
str20 = "Python is a Interpreted Language" 
print(str20.startswith("Python"))

'''# swapcase() : The swapcase() method returns a string where all the upper case letters are lower case and vice versa.'''
str21 = "Python is a Interpreted''' Language" 
print(str21.swapcase())

'''# title() : The title() method returns a string where the first character in every word is upper case.'''
str22 = "He's name is Dan. Dan is an honest man."
print(str22.title())