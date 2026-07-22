def greet(fname , lname):
    print("Hello" , fname , lname)

name = "BB"
last = "JJ"

greet(name , last)

# If you want to pass the function then use the "pass" 
'''def pas():
    pass
'''
def calMean(a , b):
    mean = (a+b)/2
    print(int(mean))

a = 9
b = 1
calMean(a , b)

# Add two number 
# let define the function first
def isum(a , b):
    sum = a + b
    print(int(sum))



# Code
a = int(input("Enter number: "))
b = int(input("Enter number: "))
isum(a,b)

# Write a function called check even or odd
# function
def check_even_odd(num):
    if num % 2 == 0:
        print("Even Number")
    
    else:
        print("Odd Number")


num = int(input("Enter the number: "))
check_even_odd(num)
    

def calmulti(a , b):
    multipily = a*b
    print("Result:",multipily)

first = int(input("Enter First the number: "))
second = int(input("Enter your second number: "))
calmulti(first , second)

def check_square(num):
    square = a ** 2
    return square

a = int(input("enter your num: "))

result = check_square(a)

print("Result", result)





