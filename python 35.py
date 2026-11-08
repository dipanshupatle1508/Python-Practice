#print multiplication table of number n using while loop

n=int(input("enter a number :-"))

a=1
table = 0

while a<=10 :
    table = a*n
    print(f"{n} x {a} = {table}")
    a +=1