x = int(input("Enter the value of x: "))
# x is the variable to match 

match x :
    # if x is 0
    case 0:
        print("x is zero")
    # case with if else condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if condition
    case _ if x < 10:
        print("x is < 10")
    # default case with only be matched if the above cases were not matched 
    # so its is basically just an else
    case _ :
        print("x")


# Practices
# 

age = int(input("Enter your age is ")) 

match age:
    case _ if age < 10  :
        print("Recommend Class 1-4")
    case _ if 10<= age <=15 :
        print("Recommend Class 5-9")
        




