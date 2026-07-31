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

"""
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

"""


# Greeting With respect to time 

"""
import time

def greet(): # ye function define karta hai bas 
    hour = int(time.strftime("%H"))

    if 5 <= hour < 12:
        print("Good Morning")
    elif 12 <= hour < 17:
        print("Good Afternoon")
    elif 17 <= hour < 21:
        print("Good Evening")
    else:
        print("Good Night")

greet() # ye function call karta hai 

"""

# Print a number from 10 to 1 in reverse order 
"""
i = 10 

while(i>0):
    print(i)
    i = i-1 

"""

# Search a element in list 

"""
key = int(input("Enter a Number = "))

l = [1,2,3,4,5,6,7,8,9,0]

if key in l:
    print("Key is Found In list")
else:
    print("Key is not found")

"""

# Print cube of number 1 to 10 using while loop 

"""
import math 

y = 3 

i = 10

while(i>0):
    print(pow(i ,y))
    i = i-1

"""

# print a even number from 1 to 100 using while loop 

"""
i = 100 

while(i>0):
    print(i)
    i= i -2 
"""

# print a positive number from a list 
"""
l = [-1,-2,-3,4,5,-8,7,-9]

for i in l:
    if(i > 0):
        print(i)
"""

# print a plus using a star 
"""
n = int(input("Enter a Number "))

mid = n//2 

for i in range(n):
    for j in range(n):
        if i == mid or j == mid :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
"""

# Print 'H' using a star 
"""
n = int(input("Enter a Number "))

mid = n//2 

for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == mid :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
"""
# print '4' using a star 

"""
n = int(input("Enter a Number "))

mid = n//2 

for i in range(n):
    for j in range(n):
        if j == n-1 or (j == 0 and i <= mid) or i == mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print( )
"""

# Calculate simple interest

import math 
"""
#This is for yearly calculator :
p = float(input("Enter a Principal amount : "))
r = float(input("Enter a Annual interest rate (percentage): "))
t = int(input("Enter a Time period (in years) : "))

SI = p*r*t/100

print(SI)
"""
"""
# This is for monthly calculator :
p = float(input("Enter a Principal amount : "))
r = float(input("Enter a Annual interest rate (percentage): "))
m = int(input("Enter a number of months : "))

SI = (p*r*m)/(12*100)

print(SI)
"""

# Grade calculator (A, B, C, D, E, F). 

"""
marks=int(input("Enter Your number for grade : "))

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
elif marks >= 50:
    print("E")
else:
    print("F")

"""

# Check whether a person is eligible to vote. 
"""
age = float(input("Enter your age : "))

if age >= 18 :
    print("You are eligible for vote Go and Drink !!")
else :
    print("You are not eligible Go and drink milk !!")

"""

# ATM Simulation :

"""
balance = 100000
correct_pin = "0329"
attempts = 3 

def check_balance():
    print(f"\nYour Current Balance : Rs. {balance}")

def deposit():
    global balance 
    amount = float(input("Enter amount to deposit : Rs. "))

    if amount > 0 :
        balance += amount 
        print("Deposit Successful!")
        print(f"Update Balance: Rs {balance}")
    else:
        print("Invalid Amount")

def withdraw():
    global balance 
    amount = float(input("Enter amount to withdraw: Rs. "))

    if amount <= 0 :
        print("invalid Amount !")

    elif amount >balance :
        print("Insufficient Balance !")

    else:
        balance -= amount 
        print("Please collect your cash.")
        print(f"Remining Balance: Rs. {balance}")

def menu():
    while True :
        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("==============================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("\nThank you for using our ATM!")
            print("Have a Nice Day!")
            break

        else : 
            print("Invalid Choice! Please try again.")


# PIN Verification


while attempts > 0:
    pin = input("Enter 4-digit ATm Pin : ") 

    if pin == correct_pin:
        print("/nLogin Successful !")
        menu()
        break 

    else:
        attempts -= 1 
        print ("Incorrect Pin! ")

        if attempts > 0 :
            print(f"Attempts Left: {attempts}")
        else:
            print("\nYour Card Has Been Blocked!")
            print("Please Contact Your Bank.")

"""

# Merge two lists. 

"""
Grp_1 = ["Anshul","Abhinav","Abhinav","CP"]
Grp_2 = ["Lalit","Akash","Ashish","Hiran"]

merge = Grp_1 + Grp_2

print(merge)
"""

# Find the sum and average of list elements.

"""
marks = [79,80,86,83,90]
X = sum(marks)
average = sum(marks) / len(marks)

print("Your Sum of List is ",X)

print("Your Average of List is ",average)
"""

# Print Fibonacci series. 

"""
n = int(input("Enter The number of terms : "))

a = 0 
b = 1 

print("Fibonacci Series: ")

for i in range(n):
    print(a , end=" ")
    c= a + b 
    a = b 
    b = c 
"""