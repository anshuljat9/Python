def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter an index: "))
        print(l[i])
        return 1 
    except :
        print("Some error occurred")
        return 0 
    finally: 
        print("This will always execute")


x = func1() 
print(x)

            
