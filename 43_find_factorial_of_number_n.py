# Find factorial of a number

#using for loop :-

n=int(input("enter a number:-"))

prod=1

for i in range(1,n+1,1):
    prod*=i
    
print(prod)

#using while loop :-

n=int(input("enter a number :-"))

prod = 1
i =1

while i<=n:
    prod *=i
    i+=1
    
print(prod)