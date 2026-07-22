''' defualt Function '''

def name(fname , mname = "Queen" , lname = "Prince"):
    print("hello" , fname , mname , lname)

name("Abby") 

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


'''Keyword argument'''

# def name(aname , bname , cname):
#     print(aname , bname, cname)


# name(bname = "Radha" , aname = "Sunshine" , cname = "Brick")

# def name(aname , bname , cname):
#     print("Hello",aname , bname, cname)

# name("peter","quilt","ididi")

'''variabl-lenght argument
Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.
'''
# def name(*name):
#     print("Hello", name[0] , name[1] , name[2])
  
# name("Radha","Bha","esh")

'''Keyword Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.'''

# def name(**name):
#     print("Hello", name["aname"] , name["bname"], name["cname"])


# name(aname = "Buchanan", bname = "Barnes", cname = "James")


'''Return Statement'''
# " " we use this for space 
def name(aname , bname , cname):
    return "hello " + aname + " " + bname + " "  + cname 
a = name("James", "Buchanan", "Barnes")

print(a)


