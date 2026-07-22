name = 'Rahul'
for name in name :
    print(name)
    if(name == "a"):     print("This is yoooooooo!!!")


animal = ["Tiger", "Lions" , "Elephant " , "Birds"]
for animal in animal:
    print(animal)
    for x in animal:
        print(x)

# range()
for k in range(1 , 21):
    print(k)

for num in range(50 ,31 , -2):
    print(num)

for num in range(5, 31 , 5):
    print(num)

for num in range(6 , 19 ,6):
    print(num)

# Loop from 1 to 20
for num in range(1, 21):
    
    # Check if the number is even (divisible by 2)
    if num % 2 == 0:
        
        # Check if the number is also divisible by 3
        if num % 3 == 0:
            
            # If both conditions are true, print the number
            print(num)

for num in range(5 , 46):
        if num % 2 != 0 :
            if num % 5 == 0:
            
                    print(num)


for num in range(1 , 100):
    if num % 2 == 0:
        if num % 7 == 0 :
            print(num)