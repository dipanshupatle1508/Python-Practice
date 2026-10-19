#Accept temperature in °C and print a description.

temp = int(input("enter temperature in °C :- "))

if temp<0 :
    print("freezing cold")
    
elif 30<temp<40 :
    print("pleasant")
    
else :
    print("very hot")
