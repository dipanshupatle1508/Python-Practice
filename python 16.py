#Factorial of a number.

a = 1   #here don;t take zero otherwise in all case output will show 0 as answer
n = int(input("put number till where you want product  :-"))

for i in range(1,n+1):
    a = a*i 
    
print(a)