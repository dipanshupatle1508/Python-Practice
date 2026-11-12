# Check whether a number is a perfect number

n=int(input("enter a number :-"))

sum =0
for i in range(1,n,1) :
    if n %i == 0 :
        sum+=i
        
if sum == n :
    print("number is perfect")
else:
    print("number is not perfect")
    
        
        
    