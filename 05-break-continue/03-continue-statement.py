#The continue statement is used in a while or for loop to take the control 
#to the top of the loop without executing the rest statements inside the loop. Here is a simple example.
for x in range(7):
    if (x == 3 or x==6):
        continue
    print(x)
