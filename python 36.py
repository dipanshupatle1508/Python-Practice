#print the sqaure of number till given number n using while loop

n=(4,5,54,65,76,34,65,9,67,5,6,43,3,34,64)
x=int(input("enter your number :-"))

i = 0

while i<len(n):
    
    if n[i]==x :
        print("founded at index", i)
    i+=1
        