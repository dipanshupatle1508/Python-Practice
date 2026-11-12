# Find factors of a number

n  =int(input("enter a number :-"))

factor = 0

for i in range(1,n,1) :
    if n%i == 0  :
        print(i)
        