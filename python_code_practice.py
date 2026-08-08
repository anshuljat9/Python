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
import os 
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

# Convert kilometers to meters.
"""
kilo = float(input("Enter a Kilometer : "))

meter = kilo * 1000 

print(meter)

"""

# Convert Celsius to Fahrenheit. 
"""
cel = int(input("Enter temprature in celsius : "))

fah = 1.8*cel + 32

print(fah) 

"""

# Login System 
"""
username = "anshuljat9"
password = "0329"

attempts = 3 

while attempts > 0 :

    user = input("Enter Your Username : ")
    pwd = input("Enter Your Password : ")

    if user == username and pwd == password:
        print("Login Successfull !!")
        break 

    else :
        attempts -= 1 

        if attempts > 0:
            print("Invalid Username or Password ")
            print("Attempts Lefts :", attempts)

        else :
            print("Your Account is Block Temporary")

"""

# FUNCTION CODES :

# Write a function to add two numbers.

"""
def Sum(a, b):
    total = a + b
    print(total)
    

Sum(150, 56)

"""

# Write a function to subtract two numbers.

"""
def Sub(a, b):
    total = a - b
    print(total)
    

Sub(150, 50)

"""

# Write a function to multiply two numbers.

"""
def Multi(a, b):
    total = a * b
    print(total)
    

Multi(150, 50)

"""

# Write a function to divide two numbers.

"""
def Div(a, b):
    total = a / b
    print(total)
    

Div(150, 50)

"""

# Write a function to find the square of a number.

"""
def sqr(n):
    square = n * n   # also use this square = n ** 2 
    print(square)
    

sqr(9)

"""

# Write a function to find the cube of a number.

"""
def cube(n):
    total = n ** 3 
    print(total)
    

cube(2)

"""

# Write a Function for calculate a power 

"""
def power(n):
    total = pow(n, 4)
    print(total)
    

power(2)

"""

# Write a function to calculate the area of a rectangle.

"""
def area_rectangle(l ,b):
    sum = l * b 
    print(sum)
    

area_rectangle(2, 6)

"""

# Write a function to calculate the area of a circle.

"""
def area_circle(r):
    sum = 3.14 * (r ** 2) 
    print(sum)

area_circle(4)

"""

# Write a function to calculate the average of three numbers.

"""
def avg(a,b,c):
    sum = (a+b+c)/3 
    print(sum)
   

avg(1,2,3)

"""

# Function to check whether a number is even or odd.
"""
# THis is without return :
def even_odd(n):
    if n % 2 == 0 :
        print(n ,"is a EVEN !")
    else:
        print(n ,"is a ODD !")


even_odd(3)

"""
"""
# This is with return :
def even_odd(n):
    if n % 2 == 0 :
        return n,'is a EVEN !'
    else:
        return n,'is a ODD !'


print(even_odd(3))

"""

# Function to check whether a number is positive, negative, or zero.

"""
def check_num(n):
    if n > 0:
        print("This is Positive number ")
    elif n < 0 :
        print("This is negative number ")
    else:
        print("This is ZERO !! ")

check_num(-2)

"""

# Function to calculate BMI.

"""

def bmi():

    weight = float(input("Enter Weight (kg): "))
    height = float(input("Enter Height (m): "))

    value = weight / (height ** 2)

    print("BMI = ",round(value, 2))
    
bmi()

"""

# Function to calculate electricity bill.

"""
def bill():

    unit = float(input("Enter your Unit : "))

    value = unit * 8.5 

    print("Your Electricity Bill is",value )

bill()

"""

# funvtion of hello ! 

"""
def greet(name):
    print("Hello", name)
a = input("Enter your name : ")

greet(a)

"""

# WAF to find factorial of a number using return .

"""
def fact(n):
    fact = 1
    for i in range(1 ,n+1):
        fact *= i 
    return fact
n = int(input("Enter a Number : ")) 

print(fact(n))

"""

# WAF to check the given number is even or odd .

"""
def even_odd(n):
    if n % 2 == 0 :
        print(n ,"is a EVEN !")
    else:
        print(n ,"is a ODD !")

even_odd(3)

"""

# WAF to calculate area of rectangle .
"""
def area_rectangle(l ,b):
    sum = l * b 
    print(sum)
    return sum 

area_rectangle(2, 6)
"""

# WAF to calculate simple interest .
"""
def STI(p, r, t):
    total = (p * r * t) / 100
    print(total)
    return total

STI(100000 , 24 ,1)

"""

# WAF to calculate a electricity bill by taking a defalut arrugemt is price of 6 rs per unit .

"""
def electricity_bill(units, price_per_unit=6):
    total_bill = units * price_per_unit
    print("Total Electricity Bill: Rs.", total_bill)
    return total_bill

electricity_bill(250)

"""

# Reverse name 
"""
name = "Anshul"
reverse_name = "".join(reversed(name))
print(reverse_name)

"""

# Reverse Number 
"""
a = "123"
reverse = "".join(reversed(a)) 
print(reverse)

"""

# File I/O :

# syntax : f = open("file_name","mode")

# read a demo file :
"""
f = open("demo.txt","r")
data = f.read
print(data)
print(type(data))
f.close()

"""

# Basic Mode of File I/O :
"""
'r' → sirf reading ke liye open karta hai (default mode), file exist karni chahiye warna error
'w' → writing ke liye open karta hai, but pehle purana content overwrite/truncate kar deta hai
'x' → naya file create karta hai writing ke liye — agar file already exist karti hai to error dega
'a' → writing ke liye open karta hai, but existing content ke end mein append karta hai, purana data safe rehta hai
'b' → binary mode (images, pdf, etc jaise non-text files ke liye)
't' → text mode (default), normal string data ke liye
'+' → same file ko read aur write dono ke liye open karta hai (e.g. 'r+', 'w+')
"""

# Read only 5 element from demo.txt 

"""
f = open("demo.txt","r")
data = f.read(5)
print(data)
print(type(data))
f.close()
"""

# Read a complete line from demo.txt 

"""
f = open("demo.txt","r")

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()
"""

# Writing a new line in demo.txt 
# 'w' and 'a' mode mai aapn file bhi create kar sakte hai agar file exist nahi karti hai to .
# Use 'w' mode :
"""
f = open("demo.txt","w") # w = puri file ko overwrite kar dega 

f.write("LE bhai 'w' (mode) ne toh puri file change kar di ")

f.close()
"""

# Use 'a' mode :
"""
f = open("demo.txt","a") # a = puri file ko overwrite nahi karega , bas end me add karega

f.write("\nLE bhai 'a' (mode) ne toh puri file ko overwrite nahi kiya , bas end me add kar diya ")

f.close()
"""

# use 'r+' mode :
"""
f = open("demo.txt","r+")
f.write("LE bhai 'r+' (mode) ne toh puri file ko overwrite nahi kiya , bas starting me add kar diya ")
print(f.read())
f.close()
"""

# use 'w+' mode :
"""
f = open("demo.txt","w+")
f.write("\nLE bhai 'w+' (mode) ne toh puri file ko overwrite kar diya")
print(f.read())
"""

# use 'a+' mode :
"""
f = open("demo.txt","a+")
f.write("\nLE bhai 'a+' (mode) ne toh puri file ko overwrite nahi kiya , bas end me add kar diya ")
print(f.read())
"""

# 'With' syntax for file handling :
"""
with open("demo.txt","r") as f:
    data = f.read()
    print(data)

with open("demo.txt","w") as f:
    f.write("New line added using 'with' syntax in 'w' mode")
"""

# Deleting a file using os module :

# syntax : os.remove("file_name") but first import os module or file exist karna chahiye warna error dega .
"""
import os

os.remove("sample.txt") # ye file delete kar dega
"""

# Create a new file "practice.txt" using python . add the following data in it .

"""
f = open("practice.txt", "w")

f.write("Hi everyone\nwe are learning file I/O\nUsing Java\nI like programming in Java.")
f.close()
"""

# WAF that replace all occurrences of "Java" with "Python" in the file "practice.txt".

"""
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

"""

# Search if the word "Learning" exists in the file or not .
"""
word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")

"""

# WAF to find in which line of the file does the word "learning" occur first. print -1 if word is not found in the file.

"""
def find_word_in_file():
    word = "learning"
    data = True 
    line_no = 1 
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return 
            line_no += 1
    return -1

find_word_in_file()
"""

# WAF to find a sum of any numbers of values using variable length argument

"""
def sum_values(*n):
    total = 0
    for i in n:
        total += i
        print("Sum is : ", total)


sum_values(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) 
"""
# WAF to find a sum of any numbers of values using keyword length argument.
"""
def sum_values(**n):
    total = 0
    for key, value in n.items():
        total += value
    print("Sum is : ", total)


sum_values(a=1, b=2, c=3, d=4, e=5)
"""

# Find the maximun number using variable length argument.

"""
def find_max(*n):
    max = n[0]
    for i in n :
        if i > max :
            max = i 
    print("Max is : ", max)

find_max(1, 20, 3, 4, 50, 6, 7, 8, 9, 10)
"""