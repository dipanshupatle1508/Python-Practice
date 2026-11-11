# Count even and odd digits

n=int(input("enter a number :-"))

num = (str(n))
even = 0 
odd = 0

for i in str(num):
    if int(i) % 2 ==0 :
        even += 1
        
    else :
        odd +=1
        
print(f"odd numbers - {odd} , even numbers - {even}")