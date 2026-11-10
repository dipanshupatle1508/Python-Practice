# Find the sum of even numbers from 1 to N

#using for loop :-

n=int(input("enter a number :-"))

sum = 0

for i in range(0,n+1,2):
    sum += i
print(sum)

#using while loop :-

n=int(input("enter a number :-"))

i=0
sum = 0

while i<=n :
    sum +=i
    i+=2
    
print(sum)