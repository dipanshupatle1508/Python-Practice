#Print sum of all even and odd numbers in a range separately.

even = 0 
odd = 0

n = int(input("enter till where you want sum :-"))

for i in range(0,n+1,2) :
    even = even + i
    odd = odd + i
    if (n % 2 == 0) :
        even = even + i
    else :
        odd = odd + i
        
print(f"even sum ={even}\n odd sum ={odd}")