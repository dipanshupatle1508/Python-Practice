# Find sum of digits

n=int(input("enter a number :-"))

sum = 0

while n>0 :
    k =(n %10)
    n = n//10
    
    sum +=k
    
print(f"sum = {sum}")
    