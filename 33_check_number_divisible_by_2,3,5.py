# Check whether a number is divisible by 2, 3, and 5

n=int(input("enter your number :-"))

num =[2,3,5]
for i in num :
    if n%i==0 :
        print(f"the given number is divisible by {i}")
        
    else :
        print("not divisible")
        
    