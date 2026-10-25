#Check if a number is prime.

n = int(input("enter the number :-"))
repeat = 0

for i in range(1,n+1):
    if n % i == 0 :
        repeat = repeat + 1
        
if repeat == 2 :
    print("prime number")
else :
    print("composite number")