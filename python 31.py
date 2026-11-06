#Check if a number is palindromic (equal to its reverse).

n =int(input("enter you number :-"))
copy = n
rev = 0

while n>0:
    rev = rev*10 + n%10
    n = n//10
    
if rev == copy :
    print("pallindrome")
    
else:
    print("not a pallindrome")