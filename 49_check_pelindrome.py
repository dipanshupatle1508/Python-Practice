# Check whether a number is a palindrome

n =int(input("enter a number :-"))

copy = n 
rev = 0

while n>0 :
    rev = rev*10 + n %10
    n //= 10
    
if rev ==copy :
    print("number is a pallindrome")
    
else:
    print("not a pallindrome")