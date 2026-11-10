# Find the sum of odd numbers from 1 to N

#using for loop :-

n=int(input("enter a number :-"))

sum = 0

for i in range(1,n+1,2):
    sum += i
    
print(sum)

#using while loop :-

n=int(input("enter a number :-"))

sum = 0
i=1

while i<=n :
    sum+=i
    i+=2
    
print(sum)