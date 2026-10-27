#Check if a string is a palindrome.

a = input("enter your word :-")
rev = ""

for i in range(len(a)-1,-1,-1):
    rev = rev + a[i]
    
if rev == a :
    print("given word is palindrome")
    
else :
    print("not a palindrome")

    