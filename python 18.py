#Print all factors of a number.

n=int(input("enter you number :-"))

for i in range(1,n+1) :
    if n % i == 0 :
        print(i)