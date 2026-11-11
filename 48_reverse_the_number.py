# Reverse a number

#using while loop 

a=int(input("enter a number :-"))
rev =0

while a>0 :
    rev =rev*10 + a %10
    a//=10
    
print(rev)


#using for loop 

n=int(input("enter a number :-"))

rev = 0
for i in range(n):
    print(i)