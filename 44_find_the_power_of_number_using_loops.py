# Find power of a number using a loop

n=int(input("enter a number here :-"))
m=int(input("enter power here :-"))
power = 1

for i in range (m):
    power *= n
    
print(f"{n} ^ {m} = {power}")
    