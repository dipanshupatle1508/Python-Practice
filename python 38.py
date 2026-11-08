n =(1,23,4,3,6,45,43,2,3,654,23,56,678,8776,56,45,6,5,3,7)

a=int(input("enter your number ="))
i=0

while i < len(n):
    if a ==n[i] :
        print("found")
        break
        
    else :
        print("not found")
    i +=1
    
print("loop ended")