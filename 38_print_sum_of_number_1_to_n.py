# Find the sum of numbers from 1 to N

n=int(input("put your input :-"))

sum = 0 

for i in range(0,n+1,1) :
    sum = sum + i
print(sum)