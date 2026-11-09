# Swap two numbers using a third variable                               

n=int(input("enter your first number :-"))
m=int(input("enter your second number :-"))

print(f"before swap :- n ={n} , m ={m}")

temp=n
n=m
m=temp

print(f"after swap :- n ={n} , m={m}")