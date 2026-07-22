i = 0 
while i < 7:
    print(i) 
    i = i + 1 
    #if i == 5:
    #    break

else: 
    print("Loop completed without break")
# The else block executes when the loop completes normally (without a break)
for x in range(5):
    print("iterarion no. {} in for loop".format(x+1))
else:
    print("else block in loop ")
    print("out of loop")