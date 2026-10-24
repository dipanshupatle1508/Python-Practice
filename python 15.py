#Sum of first n natural numbers.

a = 0 
n = int(input("till how much number you want to add :- "))

for i in range(1,n+1):
    a = a + i
print(a)