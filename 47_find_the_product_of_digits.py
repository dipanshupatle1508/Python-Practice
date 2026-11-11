# Find product of digits

n=int(input("enter a number :-"))

prod=1
while n>0 :
   k = n % 10
   n //=10
   prod*=k
   
print(prod)