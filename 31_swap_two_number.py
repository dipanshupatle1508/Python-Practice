# Swap two numbers without a third variable

n=int(input("enter your number :-"))
m=int(input("enter second number :-"))

print(f"before swaping - n = {n} ,m= {m}")

n=n+m
m=n-m
n=m-n

print(f"after swap - n={n} , m={m}")
