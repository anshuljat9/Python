print("Hello, Anshul!")

# print all data type 
"""
a = [10 , 20 , 'anshul']
print(type(a)) 
b = (10 , 20 , 'anshul')
print(type(b))
c = {10 , 20 , 'anshul'}
print(type(c))
d = frozenset({10 , 20 , 'anshul'})
print(type(d))
e = {'name' : 'anshul', 'age' : '18'}
print(type(e))

"""

# print all arithmatic operator 

"""
a = 10 
b = 5 

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

"""

# largest of 2 number 

"""
a = int(input("Enter a Value of a : "))
b = int(input("Enter a Value of b : "))

c = a if a>b else b 
print("largest Number is : " , c )
 
"""

# largest of 3 number 
"""
a = int(input("Enter a Value of a : "))
b = int(input("Enter a Value of b : "))
c = int(input("Enter a Value of c : "))

d = a if (a > b and a > c) else (b if b > c else c)
print("largest Number is : " , d )

"""

# calculate distance betwwen two points 

"""
import math 

x1 = int(input("Enter the value for x1 : "))
x2 = int(input("Enter the value for x2 : "))
y1 = int(input("Enter the value for y1 : "))
y2 = int(input("Enter the value for y2 : "))

a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(a)

"""

# calculate area of circle 

"""
import math as m 

r = int(input("Enter a Radius value : "))

a = m.pi * r**2 
print(a)

"""

# Check year is leap year or not 

"""
year = int(input("Enter a Year : "))

if (year%4==0) :
    print(year, "is a leap year")
else :
    print(year, "is not a leap year")

"""

# Swap 2 number 

"""
a = int(input("Enter a value of a : "))
b = int(input("Enter a value of b : "))

print("Before Swaping a = ", a, "b = ", b)

a, b = b, a 

print("After Swaping a = ", a, "b = ", b)

"""

# Sum of two number 

"""
a = int(input("Enter a value of a = "))
b = int(input("Enter a value of b = "))

sum = ("Sum is = ", a+b )

"""

#check even or odd 

"""
a = int(input(" Enter a Number : "))

if a % 2 == 0 :
    print("Even")
else : 
    print("Odd")

"""

# Multiple Table :

"""
a = int(input("Enter a Number for Multiple Table : "))

for i in range(1,11):
    print(a, "*", i, "=", a*i)


"""

# Finding HCF anf LCM 

"""
a = int(input("Enter a Value of a : "))
b = int(input("Enter a value of b : "))

def hcf(a,b):
    while b : 
        a, b = b , a % b
    return a 


def lcm(a,b):
    return (a * b) // hcf(a,b)


print("HCF is : ", hcf(a, b))
print("LCM is : ", lcm(a, b))

"""

# Finding Average 

"""
a = [29, 3 , 20 , 7]

total = sum(a)
count = len(a)

average = total / count 

print("List is ", a)
print("Sum is ", total)
print("count is ", count)
print("Average is ", average)

"""

# print a thank you when user id is arya and password is pyhton 

"""
user = input("Enter your id : ")
password = input("Enter your passwors : ") 

if(user == 'arya' and password == 'python') :
    print("Thank you to visit Our Website ")
else:
    print("Sorry!, Try again")

"""

# Check given number is between 1 to 100 

"""
num = int(input("Enter a Number : "))

if(1 <= num <= 100) :
    print("Yes number is found")
else:
    print("Number is not found")

"""

# display number from 0 to 10 

"""
for i in range (11):
    print(i)

"""

# display 10 to 1 in desecending order 

"""
for i in range(10, 0, -1):
    print(i)

"""

# Take a single digit and print value in english 

"""
num = int(input("Enter a Numberin between 0 to 9 = "))

if(num == '0'):
    print("Zero")
elif(num == 1):
    print("One")
elif(num == 2):
    print("Two")
elif(num == 3):
    print("Three")
elif(num == 4):
    print("Four")
elif(num == 5):
    print("Five")
elif(num == 6):
    print("Six")
elif(num == 7):
    print("Seven")
elif(num == 8):
    print("Eight")
elif(num == 9):
    print("Nine")

else:
    print("Enter a Correct number from 0 to 9 ")

"""

# Calculate elctricity Bill

"""
unit = int(input("Enter your electricity unit : "))

if unit <= 100:
    bill = unit * 5
    print(bill)

elif unit <= 200:
    bill = (100 * 5) + (unit - 100) * 7
    print(bill)

else:
    bill = (100 * 5) + (100 * 7) + (unit - 200) * 10
    print(bill)

"""

# Check number is postive , negative and zero 

"""
num = int(input("Enter Your number : "))

if(num > 0):
    print(num," is a Positive Number")
elif(num < 0):
    print(num,"is a Negative Number")
else:
    print("Number is ZERO!!!")  

"""

# Role a Dice 

import random

print("Welcome to Play a Dice game")

choice = input("You want to Play a game (Y ,N) : ").lower()

if choice == "y":
    dice = random.randint(1,6)
    print(dice)

elif choice == "n":
    print("Thank You to visit our game !!!")

else:
    print("Invalid input! Please enter Y or N.")