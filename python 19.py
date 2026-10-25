#Check if a number is perfect (sum of factors = the number itself)

n= int(input("enter you number :-"))


var = 0
for i in range(1,n):
    if n % i == 0:
        var = var + i 
        
if var == n:
    print("perfect")
    
else :
    print("not perfect")
    