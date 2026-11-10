# Print multiplication tables from 1 to n 

n=int(input("enter your number :-"))

for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        print(f"{i} x {j} = {j*i}")